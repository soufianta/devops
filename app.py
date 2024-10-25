import requests as re
import json

req = re.get("https://api.apis.guru/v2/list.json")

try:
  js = json.loads(req.text)
  print(js)
except json.JSONDecodeError as err:
  print("invalid json data")
finally:
  print("it's ok...")