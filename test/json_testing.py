import io
import json

p = io.open("test_json.json", 'r')
data: list = json.loads(p.read())
p.close()

data.append({"id": 4, "name": "Pedro", "edad": 34})

p = io.open("test_json.json", "w+")
p.write(json.JSONEncoder().encode(data))
