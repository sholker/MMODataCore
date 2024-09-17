# MMODataCore MMORPG Project

## Overview

This project is designed to manage and analyze data for the MMODataCore MMORPG. It utilizes MongoDB to store and query data related to players, quests, and player actions. The system provides functionalities to analyze player behaviors, quest difficulties, and shared quest statistics.

## Components

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

### QueryHandlerFactory

`QueryHandlerFactory` is responsible for providing appropriate query handler instances based on the collection type. It centralizes the creation of query handlers, allowing the rest of the application to obtain handlers for different collections without needing to know the details of their implementation.

### BaseQueryHandler

`BaseQueryHandler` serves as a base class for all query handlers. It encapsulates common functionalities for querying and manipulating MongoDB collections, such as inserting data and checking for duplicates. This class ensures that all query handlers share a consistent interface and behavior.

### QueryType (Enum)

`QueryType` is an enumeration that defines the different types of queries that can be performed on MongoDB collections. Examples include `INSERT_ONE`, `FIND`, `UPDATE_ONE`, and others. This enum helps to standardize query operations and makes the code more readable and maintainable.

### CollectionType (Enum)

`CollectionType` is an enumeration that represents the different types of collections in the MongoDB database. This enum is used to categorize collections, such as `PLAYER`, `QUEST`, `PLAYER_ACTION`, and `SHARED_QUEST`. It assists in managing and referencing collections throughout the project.

### MongoConnector

`MongoConnector` is a utility class that handles the connection to the MongoDB database. It manages connection pooling and provides methods to get database and collection instances. This class ensures that the connection details are centralized and can be easily managed.

### MongoCollectionHandler

`MongoCollectionHandler` is responsible for managing interactions with a specific MongoDB collection. It provides methods to perform common operations like querying, inserting, and updating documents. This class abstracts the MongoDB operations and allows for easy manipulation of collection data.

### PlayerQueryHandler

`PlayerQueryHandler` is a specialized query handler for the `player` collection. It inherits from `BaseQueryHandler` and provides methods specific to querying and analyzing player data. For instance, it includes functionality to fetch players with a minimum level or to find the highest level player per country.

### QuestsQueryHandler

`QuestsQueryHandler` is a specialized query handler for the `quest` collection. It inherits from `BaseQueryHandler` and provides methods for querying quest data. This includes functionality to retrieve quest details, analyze quest completion rates, and other quest-related statistics.

### PlayerActionQueryHandler

`PlayerActionQueryHandler` is a specialized query handler for the `player_action` collection. It inherits from `BaseQueryHandler` and provides methods specific to analyzing player actions. This includes functionality for calculating dropout rates based on action types or quest difficulties.


### SharedQuestsQueryHandler

`SharedQuestsQueryHandler` is a specialized query handler for the `shared_quests` collection. It provides methods to analyze shared quests, such as counting quests involving players from different countries versus those from the same country.

## Functions

### `load_data(directory)`

Loads data from JSON files in the specified directory into the MongoDB collections.

### `analyze_early_quests_dropout_rate()`

Analyzes and displays the dropout rates for quests based on difficulty.

### `analyze_shared_quests_by_country()`

Analyzes and displays statistics for shared quests, including counts of quests involving players from different countries versus the same country.

### `analyze_players_with_min_level(min_level)`

Analyzes and displays players with a level greater than or equal to the specified minimum level.

### `analyze_highest_level_per_country()`

Analyzes and displays the highest level players per country.

## Setup

1. **Install Dependencies**: Ensure you have the required Python packages installed. You can use `pip` to install dependencies from a `requirements.txt` file if provided.

2. **Configure MongoDB**: Make sure your MongoDB server is running and properly configured.

3. **Run Scripts**: Use the provided functions to load data, create indexes, and analyze data.

```bash
python main.py
```
For more information, please visit our [documentation]([Final Project - NoSql.pdf](Docs%2FFinal%20Project%20-%20NoSql.pdf)).
