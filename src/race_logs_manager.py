import json
from utility import input_date
from validator import validate_race_log

# Allow user to add race results which will be stored in json file
def add_race_log():
    horse_name = input("Enter horse name: ")
    race_date_obj = input_date("Enter race date (DD-MM-YYYY): ")  # Returns a datetime.date object
    race_date = race_date_obj.strftime('%d-%m-%Y')  # Converts the datetime.date object to a string
    race_result = input("Enter race result: ")

    new_log = {"HorseName": horse_name, "RaceDate": race_date, "RaceResult": race_result}

# Validate the data entry from the user to ensure that it matches
# against the specified schema, else return error message
    if validate_race_log(new_log):
        with open('data.json', 'r+') as file:
            data = json.load(file)
            data['race_logs'].append(new_log)
            file.seek(0)
            file.truncate()
            json.dump(data, file)
    else:
        print("Invalid race log")

# Display race logs to user from the json file database
def view_race_logs():
    with open('data.json', 'r') as file:
        data = json.load(file)
        for log in data['race_logs']:
            print(log)
