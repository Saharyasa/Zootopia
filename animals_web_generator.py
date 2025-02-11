import json
import os

# Step 1: Load the JSON data with error handling
def load_data(file_name):
    """Loads a JSON file and returns the parsed data with error handling."""
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    file_path = os.path.join(current_directory, file_name)  # Full path to JSON file

    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"❌ Error: The file {file_name} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"❌ Error: The file {file_name} contains invalid JSON.")
        return []

# Step 2: Serialize a single animal object safely
def serialize_animal(animal):
    """Converts an animal object into an HTML list item format."""
    output = "<li class='cards__item'>\n"
    output += f"    <div class='card__title'>{animal.get('name', 'Unknown')}</div>\n"
    output += "    <p class='card__text'>\n"
    output += f"        <strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', 'Unknown')}<br/>\n"

    # Add location if available (only the first location)
    locations = animal.get("locations", [])
    if locations:
        output += f"        <strong>Location:</strong> {locations[0]}<br/>\n"  # Use only the first location

    # Add type if available
    output += f"        <strong>Type:</strong> {animal.get('characteristics', {}).get('type', 'Unknown')}<br/>\n"

    output += "    </p>\n"
    output += "</li>\n"  # Close list item

    return output

# Step 3-6: Load JSON, generate HTML content, and write output file
def main():
    # Load the JSON file and generate HTML content
    animals_data = load_data("animals_data.json")
    animals_html_content = "".join([serialize_animal(animal) for animal in animals_data])

    # Read the HTML template file
    try:
        with open("animals_template.html", "r") as template_file:
            html_template = template_file.read()
    except FileNotFoundError:
        print("❌ Error: animals_template.html was not found.")
        return

    # Replace the placeholder with the generated animal data
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html_content)

    # Write the modified HTML to a new file (animals.html)
    with open("animals.html", "w") as output_file:
        output_file.write(html_output)

    print("✅ HTML file generated successfully: animals.html")

