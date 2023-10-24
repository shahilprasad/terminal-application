# Defining the data structure for horse data
horse_schema = {
    "type": "object",
    "properties": {
        "Name": {"type": "string"},
        "Age": {"type": "number"},
        "Health": {"type": "string"},
        "Diet": {"type": "string"}
    },
    "required": ["Name", "Age", "Health", "Diet"]
}

# Defining the data structure for race logs
race_log_schema = {
    "type": "object",
    "properties": {
        "HorseName": {"type": "string"},
        "RaceDate": {"type": "string", "format": "date"},
        "RaceResult": {"type": "string"}
    },
    "required": ["HorseName", "RaceDate", "RaceResult"]
}
