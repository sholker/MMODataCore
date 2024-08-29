from enum import Enum

class CollectionType(Enum):
    PLAYER = "player"
    PLAYER_ACTION = "player_action"
    QUEST = "quest"
class QueryType(Enum):
    FIND = "find"
    AGGREGATE = "aggregate"
    MAP_REDUCE = "map_reduce"
    INSERT_ONE = "insert_one"
    INSERT_MANY = "insert_many"
    DELETE = "delete"
    UPDATE = "update"
    UPDATE_ONE = "update_one"
    UPDATE_MANY = "update_many"
