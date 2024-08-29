from mongoDB.queryHandler import BaseQueryHandler,PlayerQueryHandler, PlayerActionQueryHandler, QuestQueryHandler

class QueryHandlerFactory:
    @staticmethod
    def get_query_handler(collection_name: str) -> BaseQueryHandler:
        if collection_name == "player":
            return PlayerQueryHandler()
        elif collection_name == "player_action":
            return PlayerActionQueryHandler()
        elif collection_name == "quest":
            return QuestQueryHandler()
        else:
            raise ValueError(f"Unknown collection name: {collection_name}")