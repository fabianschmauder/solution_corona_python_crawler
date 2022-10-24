import json

def save_data_to_file(data):
    with open("corona-data.json","w") as file:
        file.write(json.dumps(data))
