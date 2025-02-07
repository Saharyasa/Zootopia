import os
import json

def load_data(file_name):
    """Loads a JSON file and returns the parsed data."""
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    file_path = os.path.join(current_directory, file_name)  # Full path to JSON file

    with open(file_path, "r") as handle:
        return json.load(handle)

# Load the JSON file
animals_data = load_data("animals_data.json")

# Iterate through the data and print specific fields
for animal in animals_data:
    print(f"\nName: {animal['name']}")
    print(f"Diet: {animal['diet']}")

    # Print location if it exists
    if "locations" in animal and len(animal["locations"]) > 0:
        print(f"Location: {animal['locations'][0]}")

    # Print type if it exists
    if "type" in animal:
        print(f"Type: {animal['type']}")
