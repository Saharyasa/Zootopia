import json
import os

# Step 1: Load the JSON data
def load_data(file_name):
    """Loads a JSON file and returns the parsed data."""
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    file_path = os.path.join(current_directory, file_name)  # Full path to JSON file

    with open(file_path, "r") as handle:
        return json.load(handle)

# Function to serialize a single animal
def serialize_animal(animal):
    """Converts an animal dictionary into an HTML string."""
    output = "<li class='cards__item'>\n"
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += "<p class='card__text'>\n"
    output += f"<strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}<br>\n"

    # Add location if available
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<strong>Location:</strong> {', '.join(animal['locations'])}<br>\n"

    # Add type if available
    if "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br>\n"

    output += "</p>\n"
    output += "</li>\n"  # Close list item
    return output

# Load the JSON file
animals_data = load_data("animals_data.json")

# Step 2: Generate a string with the animals’ data
output = ''.join([serialize_animal(animal) for animal in animals_data])

# Step 3: Read the HTML template file
with open("animals_template.html", "r") as template_file:
    html_template = template_file.read()

# Step 4: Replace the placeholder with the generated animal data
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 5: Write the modified HTML to a new file (animals.html)
with open("animals.html", "w") as output_file:
    output_file.write(html_output)

print("✅ HTML file generated successfully: animals.html")
