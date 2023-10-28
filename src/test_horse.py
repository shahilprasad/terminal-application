import pytest
from validator import validate_horse

# Test 1: Validate correct horse schema
def test_validate_correct_horse_schema():
    # Test that the validate_horse function correctly validates correct horse data.
    valid_horse_data = {
        "Name": "Starlight",
        "Age": 5,
        "Health": "Healthy",
        "Diet": "Hay and grass"
    }
    assert validate_horse(valid_horse_data) == True

# Test 2: Validate incorrect horse schema
def test_validate_incorrect_horse_schema():
    # Test that the validate_horse function correctly identifies incorrect horse data.
    invalid_horse_data = {
        "Name": 12345,  # Invalid name, should be a string
        "Age": "Five",  # Invalid age, should be a number
        "Health": "Healthy",
        "Diet": "Hay, grass, and water",
    }
    assert validate_horse(invalid_horse_data) == False

# Test 3: Validate missing fields in horse schema
def test_validate_missing_fields_in_horse_schema():
    # Test that the validate_horse function identifies when some required fields are missing.
    # Invalid horse data (missing required field "Diet")
    invalid_horse_data = {
        "Name": "Lucky",
        "Age": 4,
        "Health": "Healthy",
    }
    assert validate_horse(invalid_horse_data) == False
