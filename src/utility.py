from datetime import datetime

# Function to ensure dates received are in the correct format
# If error raised user will be prompted to enter a valid date
def input_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, '%d-%m-%Y').date()
        except ValueError:
            print("Incorrect format, should be DD-MM-YYYY")

# Functiion to ensure an integer is returned when obtaining age
# If error raised user will be prompted to enter a valid number
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
