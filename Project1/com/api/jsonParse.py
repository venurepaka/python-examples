import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

parsed_json_obj = json.loads(json_string)
print parsed_json_obj["first_name"]

parsed_json_str = json.dumps(parsed_json_obj)
print parsed_json_str

