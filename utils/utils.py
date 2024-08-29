import json
def load_data_from_file(file_path: str) -> json:
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
    return []


def print_table(data):
    if not data:
        print("No data to display.")
        return

    # Determine the column headers
    headers = set()
    for row in data:
        headers.update(row.keys())
    headers = sorted(headers)  # Sort headers for consistent column order

    # Determine the column widths
    column_widths = {header: max(len(header), max(len(str(row.get(header, ""))) for row in data)) for header in headers}

    # Create a format string for rows
    row_format = " | ".join([f"{{:<{column_widths[header]}}}" for header in headers])

    # Print the header row
    print(row_format.format(*headers))
    print("-" * (sum(column_widths.values()) + 3 * len(headers) - 1))

    # Print each data row
    for row in data:
        print(row_format.format(*[str(row.get(header, "")) for header in headers]))
