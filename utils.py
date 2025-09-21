#!/usr/bin/env python
import json

def modifyUser(user):
    with open("./users/users.json", "r") as f:
        data = json.load(f)

    data[user] = False

    with open("./users/users.json", "w") as f:
        json.dump(data, f, indent=4)
