from pymongo import errors
from mongoDB.enums import QueryType
from mongoDB.mongoCollectionHandler import MongoCollectionHandler
import json

class BaseQueryHandler:
    def __init__(self, collection_name: str):
        self.collection_handler = MongoCollectionHandler(collection_name)

    def check_for_duplicate(self, document):
        """Check if an identical document already exists in the collection."""
        try:
            # Query to match the entire document
            query = {k: v for k, v in document.items()}
            return self.collection_handler.run_query(QueryType.FIND,query=query) is not None
        except errors.PyMongoError as e:
            print(f"An error occurred while checking for duplicates: {e}")
            return False

    def create_indexes(self):
        """Create indexes for the collection based on the INDEXES configuration."""
        try:
            collection = self.collection_handler.collection
            indexes = self.INDEXES.get(self.collection_handler.collection_name, [])
            for index in indexes:
                key = index['key']
                unique = index.get('unique', False)
                collection.create_index(key, unique=unique)
            print(f"Indexes created for {self.collection_handler.collection_name}.")
        except Exception as e:
            print(f"An error occurred while creating indexes: {e}")

    def insert_data(self, data):
        """Insert data into the collection, avoiding duplicates."""
        try:
            if isinstance(data, dict):
                # Check for duplicate
                if self.check_for_duplicate(data):
                    # print(f"Document with {self.unique_field} {data.get(self.unique_field)} already exists.")
                    return None
                result = self.collection_handler.run_query(QueryType.INSERT_ONE, update=data)
                # print(f"Document inserted with ID: {result.inserted_id}")
                return result.inserted_id
            elif isinstance(data, list):
                # Check for duplicates and insert data
                insert_results = []
                for item in data:
                    if not self.check_for_duplicate(item):
                        result = self.collection_handler.run_query(QueryType.INSERT_ONE, update=item)
                        insert_results.append(result.inserted_id)
                        # print(f"Document inserted with ID: {result.inserted_id}")
                    # else:
                    #     print(f"Document with {self.unique_field} {item.get(self.unique_field)} already exists.")
                return insert_results
            else:
                raise TypeError("Data must be a dictionary or list of dictionaries")
        except TypeError as e:
            print(f"Type error: {e}")
        except errors.PyMongoError as e:
            print(f"An error occurred while inserting data: {e}")