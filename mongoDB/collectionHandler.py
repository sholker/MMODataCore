from mongoDB.mongoCollectionHandler import MongoCollectionHandler

from enums import CollectionType

# todo: rename
class PlayerActionsHandler(MongoCollectionHandler):
    def __init__(self):
        super().__init__(CollectionType.PLAYER)


class PlayerActionHandler(MongoCollectionHandler):
    def __init__(self):
        super().__init__(CollectionType.PLAYER_ACTION)


class QuestDataHandler(MongoCollectionHandler):
    def __init__(self):
        super().__init__(CollectionType.QUEST)
