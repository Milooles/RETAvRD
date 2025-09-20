import json

with open("./users/users.json", "r") as f:
    data = json.load(f)

data["011935"] = True

with open("./users/users.json", "w") as f:
    json.dump(data, f, indent=4)
