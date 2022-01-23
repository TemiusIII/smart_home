import json
config = json.load(open('config_undecoded.json', 'r', encoding='utf-8'))
print(config['name'])