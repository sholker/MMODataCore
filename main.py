import os
from prettytable import PrettyTable
from mongoDB.queryHandlerFactory import QueryHandlerFactory as queryHandler
from utils.utils import load_data_from_file

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
        table = PrettyTable()
        table.field_names = ["Difficulty", "Dropout Rate (%)"]
        for group in dropout_rate_by_difficulty:
            difficulty = group['_id']
            dropout_rate = group.get('dropout_rate', 0.0)
            table.add_row([difficulty, f"{dropout_rate:.2f}"])

        print("Dropout rate by quest difficulty:")
        print(table)

    except Exception as e:
        print(f"An error occurred while analyzing dropout rates: {e}")


def analyze_shared_quests_by_country():
    try:
        # Get the singleton instance
        shared_quests_handler = collection_handlers.get("shared_quests")
        if not shared_quests_handler:
            collection_handlers["shared_quests"] = queryHandler.get_query_handler("shared_quests")
            shared_quests_handler = collection_handlers.get("shared_quests")

        print("Analyzing shared quests by country...")

        # Fetch stats for shared quests
        shared_quests_stats = shared_quests_handler.get_shared_quests_country_stats()

        # Display the results
        if shared_quests_stats:
            stats = shared_quests_stats[0]
            table = PrettyTable()
            table.field_names = ["Metric", "Count"]
            table.add_row(["Total Shared Quest Combinations (Different Countries)",
                           stats['total_shared_quest_combinations_different_county']])
            table.add_row(
                ["Shared Quest Combinations (Same Country)", stats['shared_quest_combinations_with_same_country']])

            print("Shared quests by country:")
            print(table)
        else:
            print("No data found for the aggregation query.")

    except Exception as e:
        print(f"An error occurred while analyzing shared quests: {e}")


def analyze_players_with_min_level(min_level=3):
    try:
        # Get the singleton instance
        player_handler = collection_handlers.get("player")
        if not player_handler:
            collection_handlers["player"] = queryHandler.get_query_handler("player")
            player_handler = collection_handlers.get("player")

        print(f"Analyzing players with level {min_level} and above...")

        # Fetch players with the minimum level
        players = player_handler.get_players_with_min_level(min_level)

        # Display the results
        if players:
            table = PrettyTable()
            table.field_names = ["Player ID", "Username", "Level"]
            for player in players:
                table.add_row([player['player_id'], player['username'], player['level']])

            print(f"Players with level {min_level} and above:")
            print(table)
        else:
            print("No players found with the specified level.")

    except Exception as e:
        print(f"An error occurred while analyzing players: {e}")


def analyze_highest_level_per_country():
    try:
        # Get the singleton instance
        player_handler = collection_handlers.get("player")
        if not player_handler:
            collection_handlers["player"] = queryHandler.get_query_handler("player")
            player_handler = collection_handlers.get("player")

        print("Analyzing highest level players per country...")

        # Fetch the highest level player per country
        players_by_country = player_handler.get_highest_level_per_country()

        # Display the results
        if players_by_country:
            table = PrettyTable()
            table.field_names = ["Country", "Username", "Level"]
            for player in players_by_country:
                table.add_row([player['country'], player['username'], player['level']])

            print("Highest level players per country:")
            print(table)
        else:
            print("No players found.")

    except Exception as e:
        print(f"An error occurred while analyzing players: {e}")


if __name__ == "__main__":
    # Uncomment to load data
    # load_data("data")

    # Analyze data
    analyze_early_quests_dropout_rate()
    analyze_shared_quests_by_country()
    analyze_players_with_min_level()
    analyze_highest_level_per_country()
