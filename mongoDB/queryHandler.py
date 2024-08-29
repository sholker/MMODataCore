from mongoDB.baseQueryHandler import BaseQueryHandler
from mongoDB.enums import QueryType
from utils.singleton import singleton
import json


@singleton
class PlayerQueryHandler(BaseQueryHandler):
    def __init__(self):
        super().__init__("player")

    def get_player_from_country(self,country_name: str) -> json:
        query = {
            "country": country_name
        }
        return self.collection_handler.run_query(QueryType.FIND, query=query)



@singleton
class PlayerActionQueryHandler(BaseQueryHandler):
    def __init__(self):
        super().__init__("player_action")

    def get_early_quests(self) -> json:
        early_quests_query = {
            "action_type": "Quest Completion",
            "difficulty": {"$gte": 3}
        }
        return self.collection_handler.run_query(QueryType.FIND, query=early_quests_query)

    def get_dropout_rate_by_difficulty(self) -> json:
        pipeline = [
            {"$match": {"action_type": "Quest Completion", "difficulty": {"$gte": 3}}},
            {"$group": {
                "_id": "$difficulty",
                "total_players": {"$sum": 1},
                "active_players": {"$sum": {
                    "$cond": [
                        {"$in": ["$player_id", self.get_active_player_ids()]},
                        1,
                        0
                    ]
                }}
            }},
            {"$project": {
                "dropout_rate": {
                    "$multiply": [
                        {"$divide": [
                            {"$subtract": ["$total_players", "$active_players"]},
                            "$total_players"
                        ]},
                        100
                    ]
                }
            }}
        ]
        return self.collection_handler.run_query(QueryType.AGGREGATE, pipeline=pipeline)

    def get_active_player_ids(self) -> list:
        # Define the query to find active players who have completed the quests
        active_players_query = {
            "action_type": "Login",
            "player_id": {"$in": self.get_player_ids_from_early_quests()}
        }
        active_players = self.collection_handler.run_query(QueryType.FIND, query=active_players_query)
        return [player['player_id'] for player in active_players if 'player_id' in player]

    def get_player_ids_from_early_quests(self) -> list:
        early_quests = self.get_early_quests()
        player_ids = []
        for quest in early_quests:
            if 'player_id' in quest:
                player_ids.append(quest['player_id'])
            elif 'player_action_id' in quest:
                player_ids.append(quest['player_action_id'])

        return player_ids


@singleton
class QuestQueryHandler(BaseQueryHandler):
    def __init__(self):
        super().__init__("quest")
