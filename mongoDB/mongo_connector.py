import pymongo
from utils.singleton import singleton


@singleton
class MongoConnector:
    MONGODB_URI = 'mongodb+srv://admin:admin@mmorpgdb.53al6.mongodb.net/'
    DB_NAME = 'mmorpgDB'

    def __init__(self, uri=None, db_name=None):
        self.uri = uri or self.MONGODB_URI
        self.db_name = db_name or self.DB_NAME
        self.client = None
        self.db = None
        self._initialize_connection()

    def _initialize_connection(self):
        try:
            self.client = pymongo.MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"Connected to database: {self.db_name}")
        except pymongo.errors.ConnectionError as e:
            print(f"Failed to connect to MongoDB: {e}")
            self.client = None
            self.db = None

    def get_db(self):
        return self.db

    def close_connection(self):
        try:
            if self.client:
                self.client.close()
                print("Connection to MongoDB closed.")
        except Exception as e:
            print(f"An error occurred while closing the connection: {e}")
