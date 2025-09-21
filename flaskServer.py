from flask import Flask, abort, send_file
import os, json
from termcolor import colored as color

USERS = {
    "011935": "Miles"
}

app = Flask("Flask Server")

def getApp():
    return app

# ?user=011935
@app.route("/<user>")
def getUser(user: str = None):
    if user is None:
        abort(400, "Bad request: missing user parameter")
    userFiles = os.listdir("./users")

    if f"{user}.sh" not in userFiles:
        open(f"./users/{user}.sh", "w").close()

    # Check if user has alreay been run
    with open("./users/users.json", "r") as f:
        data = json.load(f)

    if data[user]:
        print(color(f"{USERS[user]} ({user})", "red"))
        return ""

    data[user] = True

    with open("./users/users.json", "w") as f:
        json.dump(data, f, indent=4)

    print(color(f"{USERS[user]} ({user})", "green"))
    return send_file(f"./users/{user}.sh", as_attachment=True)
