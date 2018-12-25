import json

key_file = open("../configure.json", "r")
json_data = json.load(key_file)
print(json_data['twitter_keys'])