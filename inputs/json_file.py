import json


def json_file(filename, converter):
    with open(filename, 'r') as file:
        raw = json.load(file)

    return converter(raw)
