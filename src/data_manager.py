import json

# Loading data from the json file to the user interface
def load_data_from_json(filename='data.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"horses": [], "races": []}

# Saving data received from the user to the json file
def save_data_to_json(data, filename='data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)