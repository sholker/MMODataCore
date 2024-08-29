from mongoDB.mongoCollectionHandler import MongoCollectionHandler as collectionHandler
import os
from mongoDB.enums import QueryType
from mongoDB.queryHandlerFactory import QueryHandlerFactory as queryHandler
from utils.utils import load_data_from_file
# Dictionary to store CollectionHandler instances
collection_handlers = {}

def load_data(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            collection_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(directory, file_name)

            print(f"Processing file: {file_path}")

            # Create DataHandler instance for each collection
            data_handler = queryHandler.get_query_handler(collection_name)

            # Create CollectionHandler instance for each collection
            if collection_name not in collection_handlers:
                collection_handlers[collection_name] = data_handler


            # Load JSON data from file
            data = load_data_from_file(file_path)

            # Insert data into the corresponding collection
            if data:  # Only insert if data was loaded successfully
                data_handler.insert_data(data)


            #  query for all and print the inserted data
            # all_data = data_handler.query_data()
            # print(f"Data in collection '{collection_name}':")
            # utils.print_table(all_data)

def analyze_early_quests_dropout_rate():
    try:
        # Get the singleton instance
        player_action_handler = collection_handlers.get("player_action")
        if not player_action_handler:
            collection_handlers["player_action"] = queryHandler.get_query_handler("player_action")
            player_action_handler = collection_handlers.get("player_action")

        print("Analyzing dropout rates...")
        # Fetch dropout rate by difficulty
        dropout_rate_by_difficulty = player_action_handler.get_dropout_rate_by_difficulty()

        # Display the results
        print("Dropout rate by quest difficulty:")
        for group in dropout_rate_by_difficulty:
            difficulty = group['_id']
            dropout_rate = group.get('dropout_rate', 0.0)
            print(f"Difficulty: {difficulty}, Dropout Rate: {dropout_rate:.2f}%")

    except Exception as e:
        print(f"An error occurred while analyzing dropout rates: {e}")




if __name__ == "__main__":
    load_data("data")
    analyze_early_quests_dropout_rate()