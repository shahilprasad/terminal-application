import json
from utility import input_int
from validator import validate_horse

# Add new horse to the database
def add_horse():
    name = input("Enter horse name: ")
    age = int(input("Enter horse age: "))
    health = input("Enter horse health status: ")
    diet = input("Enter horse diet: ")
    new_horse = {"Name": name, "Age": age, "Health": health, "Diet": diet}

# Validate the data entry from the user to ensure that it matches
# against the specified schema, else return error message
    if validate_horse(new_horse):
        with open('data.json', 'r+') as file:
            data = json.load(file)
            data['horses'].append(new_horse)
            file.seek(0)
            file.truncate()
            json.dump(data, file)
    else:
        print("Invalid horse data")

# Remove a horse from the database after checking the database
# for a matching horse name, else return error message
def remove_horse():
    horse_name = input("Enter the name of the horse to remove: ")
    with open('data.json', 'r+') as file:
        data = json.load(file)
        horses = data['horses']
        for horse in horses:
            if horse['Name'] == horse_name:
                horses.remove(horse)
                file.seek(0)
                file.truncate()
                json.dump(data, file)
                print(f"Horse {horse_name} removed successfully!")
                return
        print(f"No horse found with the name {horse_name}.")

# Provide option to update horse details in the database
# which will overwrite existing informatiom if match found
def update_horse_details():
    horse_name = input("Enter the name of the horse to update: ")
    with open('data.json', 'r+') as file:
        data = json.load(file)
        horses = data['horses']
        for horse in horses:
            if horse['Name'] == horse_name:
                print("Enter new details (or press Enter to skip updating):")
                name = input(f"Name (current: {horse['Name']}): ")
                age = input_int(f"Age (current: {horse['Age']}): ")
                health = input(f"Health (current: {horse['Health']}): ")
                diet = input(f"Diet (current: {horse['Diet']}): ")
                
                if name: horse['Name'] = name
                if age: horse['Age'] = int(age)
                if health: horse['Health'] = health
                if diet: horse['Diet'] = diet
                
                file.seek(0)
                file.truncate()
                json.dump(data, file)
                print(f"Horse {horse_name} details updated successfully!")
                return
        print(f"No horse found with the name {horse_name}.")

# Option for user to view all horses stored in the database
def view_all_horses():
    with open('data.json', 'r') as file:
        data = json.load(file)
        for horse in data['horses']:
            print(horse)
