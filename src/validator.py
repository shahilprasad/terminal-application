# import jsonschema
from schemas import horse_schema, race_log_schema

# File utilises the jsonschema library to validate data entries
# against the specified schemas
def validate_horse(data):
    try:
        jsonschema.validate(instance=data, schema=horse_schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation error: {e}")
        return False

def validate_race_log(data):
    try:
        jsonschema.validate(instance=data, schema=race_log_schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation error: {e}")
        return False
