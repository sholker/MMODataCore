from mongoDB.baseQueryHandler import BaseQueryHandler
from mongoDB.enums import QueryType
from utils.singleton import singleton
import json


@singleton
class PlayerQueryHandler(BaseQueryHandler):
    INDEXES = {
        'player': [
            {'key': [('player_id', 1)], 'unique': True},
            {'key': [('level', 1)]}
        ]
    }

    def __init__(self):
        super().__init__('player')
        # Create indexes after ensuring collection creation
        self.create_indexes()


    def get_player_from_country(self,country_name: str) -> json:
        query = {
            "country": country_name
        }
        return self.collection_handler.run_query(QueryType.FIND, query=query)

    def get_players_with_min_level(self, min_level: int) -> json:
        """Retrieve players with a level greater than or equal to `min_level`."""
        query = {
            "level": {"$gte": min_level}
        }
        projection = {
            "_id": 0,
            "player_id": 1,
            "username": 1,
            "level": 1
        }
        return list(self.collection_handler.run_query(QueryType.FIND, query=query, projection=projection))

    def get_highest_level_players_by_country(self):
        """Retrieve the highest level player for each country."""
        pipeline = [
            {
                "$group": {
                    "_id": "$country",  # Group by country
                    "highest_level_player": {"$first": "$$ROOT"},  # Keep the first document in each group
                    "max_level": {"$max": "$level"}  # Calculate the maximum level
                }
            },
            {
                "$project": {
                    "_id": 0,  # Exclude the _id field
                    "country": "$_id",  # Include country field
                    "username": "$highest_level_player.username",  # Include the username of the highest level player
                    "level": "$max_level"  # Include the maximum level
                }
            }
        ]
        return list(self.collection.run_query(QueryType.AGGREGATE, pipeline=pipeline))



@singleton
class PlayerActionQueryHandler(BaseQueryHandler):
    INDEXES = {
        'player_action': [
            {'key': [('player_id', 1), ('action_type', 1)]},
            {'key': [('quest_id', 1)]}
        ]
    }
    def __init__(self):
        super().__init__("player_action")
        self.create_indexes()

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
    INDEXES = {
        'quest': [
            {'key': [('quest_id', 1)], 'unique': True}
        ]
    }
    def __init__(self):
        super().__init__("quest")
        self.create_indexes()

@singleton
class SharedQuestsQueryHandler(BaseQueryHandler):
    INDEXES = {
        'shared_quests': [
            {'key': [('player_ids', 1)]}
        ]
    }
    def __init__(self):
        super().__init__("shared_quests")
        self.create_indexes()

    def get_shared_quests_country_stats(self):
        """Retrieve stats for shared quests involving players from different countries vs. the same country."""
        pipeline = [
            {"$unwind": "$player_ids"},
            {
                "$lookup": {
                    "from": "player",
                    "localField": "player_ids",
                    "foreignField": "player_id",
                    "as": "player_info"
                }
            },
            {"$unwind": "$player_info"},
            {
                "$group": {
                    "_id": "$quest_id",
                    "countries": {"$addToSet": "$player_info.country"}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total_shared_quest_combinations_different_county": {"$sum": 1},
                    "shared_quest_combinations_with_same_country": {
                        "$sum": {
                            "$cond": [{"$eq": [{"$size": "$countries"}, 1]}, 1, 0]
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "total_shared_quest_combinations_different_county": 1,
                    "shared_quest_combinations_with_same_country": 1
                }
            }
        ]

        return list(self.collection_handler.run_query(QueryType.AGGREGATE, pipeline=pipeline))

