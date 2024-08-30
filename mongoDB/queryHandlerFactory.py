from mongoDB.queryHandler import BaseQueryHandler,PlayerQueryHandler, PlayerActionQueryHandler, QuestQueryHandler
from mongoDB.enums import CollectionType
class QueryHandlerFactory:
    @staticmethod
    def get_query_handler(collection_name: str) -> BaseQueryHandler:
        if collection_name == CollectionType.PLAYER.value:
            return PlayerQueryHandler()
        elif collection_name == CollectionType.PLAYER_ACTION.value:
            return PlayerActionQueryHandler()
        elif collection_name == CollectionType.QUEST.value:
            return QuestQueryHandler()
        else:
            raise ValueError(f"Unknown collection name: {collection_name}")