# MongoDB Project

## Overview

This project is designed to manage and analyze data in MongoDB collections for an online multiplayer game. It includes functionalities for loading data, querying MongoDB collections, and analyzing specific data metrics such as player levels and shared quests.

## Components

### `QueryHandlerFactory`

The `QueryHandlerFactory` class is responsible for creating instances of query handlers based on the collection name. It abstracts the process of obtaining the appropriate handler for each collection, ensuring that the correct query logic is applied.

### `BaseQueryHandler`

The `BaseQueryHandler` class provides a base implementation for handling queries in MongoDB. It includes methods for checking duplicates before inserting data and for inserting data into the collection. It serves as a foundation for more specific query handlers.

#### Methods:
- `check_for_duplicate(document)`: Checks if a document already exists in the collection.
- `insert_data(data)`: Inserts data into the collection, avoiding duplicates.

### `QueryType` (Enum)

The `QueryType` enum defines the types of queries that can be executed on the MongoDB collections. Common query types include:
- `FIND`: Used for querying documents.
- `INSERT_ONE`: Used for inserting a single document.
- `UPDATE_ONE`: Used for updating a single document.
- `DELETE_ONE`: Used for deleting a single document.

### `CollectionType` (Enum)

The `CollectionType` enum defines the types of collections available in the project. It helps in identifying the collection type when creating query handlers. Common collection types include:
- `PLAYER`
- `QUEST`
- `PLAYER_ACTION`
- `SHARED_QUEST`

### `MongoConnector`

The `MongoConnector` class is responsible for establishing and managing the connection to the MongoDB database. It ensures that all interactions with the database are handled efficiently and securely.

### `MongoCollectionHandler`

The `MongoCollectionHandler` class manages operations on a specific MongoDB collection. It provides methods for performing CRUD operations and executing queries. This class is used to interact with the collection specified during its initialization.

### `PlayerQueryHandler`

The `PlayerQueryHandler` class inherits from `BaseQueryHandler` and provides specialized query functionalities for the `player` collection. It includes methods for querying player data based on specific criteria, such as fetching players with a minimum level.

### Functions

#### `load_data(directory)`

Loads JSON data from the specified directory into the corresponding MongoDB collections. It processes each file and inserts the data into the appropriate collection.

#### `analyze_early_quests_dropout_rate()`

Analyzes the dropout rates of players based on quest difficulty. It retrieves dropout rate statistics and displays them.

#### `analyze_shared_quests_by_country()`

Analyzes shared quests to determine the number of shared quests involving players from different countries versus the same country.

#### `analyze_players_with_min_level(min_level=3)`

Analyzes and displays players with levels equal to or above the specified minimum level.

#### `analyze_highest_level_per_country()`

Analyzes and displays the highest level players per country.

## Getting Started

1. **Install Dependencies**

   Ensure you have the required dependencies installed. You can use the `requirements.txt` file provided:

   ```bash
   pip install -r requirements.txt
