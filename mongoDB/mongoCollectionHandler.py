from mongoDB.mongo_connector import MongoConnector
from mongoDB.enums import QueryType

class MongoCollectionHandler:
    def __init__(self, collection_name):
        self.connector = MongoConnector()
        self.db = self.connector.get_db()
        self.collection_name = collection_name
        self.collection = self.db[collection_name]
        self.unique_field = f"{collection_name}_id"



    def create_collection(self):
        """Create the collection if it doesn't exist."""
        try:
            # MongoDB automatically creates the collection when data is inserted
            print(f"Collection '{self.collection_name}' is ready to use.")
        except Exception as e:
            print(f"An error occurred while creating the collection: {e}")



    def run_query(self, query_type: QueryType, query=None, projection=None, update=None, pipeline=None,
                  map_reduce=None):
        try:

            if query_type == QueryType.FIND:
                result = list(self.collection.find())
            elif query_type == QueryType.AGGREGATE:
                result = list(self.collection.aggregate(pipeline))
            elif query_type == QueryType.MAP_REDUCE:
                result = self.collection.map_reduce(map_reduce["map"], map_reduce["reduce"], map_reduce["out"])
            elif query_type == QueryType.INSERT_ONE:
                result = self.collection.insert_one(query)
            elif query_type == QueryType.INSERT_MANY:
                result = self.collection.insert_many(query)
            elif query_type == QueryType.DELETE:
                result = self.collection.delete_many(query)
            elif query_type == QueryType.UPDATE_MANY:
                result = self.collection.update_many(query, update)
            elif query_type == QueryType.UPDATE_ONE:
                result = self.collection.update_one(query, {"$set": update})
            else:
                result = None

            # print(f"Result: {result}")
            return result
        except Exception as e:
            print(f"An error occurred while running the query: {e}")
            return None

