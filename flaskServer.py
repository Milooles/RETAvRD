from flask import Flask, abort, send_file, request
from termcolor import colored as color
import os, json, utils

USERS = {
    "011935": "Miles"
}

USERS_FOLDER = "./users"
USERS_JSON = f"{USERS_FOLDER}/users.json"
BASH = f"{USERS_FOLDER}/bash"
PYTHON = f"{USERS_FOLDER}/python"

app = Flask("Flask Server")

def getApp():
    return app

# ?user=011935
@app.route("/<user>")
def getUser(user: str = None):
    if user is None:
        abort(400, "Bad request: missing user parameter")
    userFiles = os.listdir(BASH)

    if f"{user}.sh" not in userFiles:
        open(f"{BASH}/{user}.sh", "w").close()

    # Check if user has alreay been run
    with open(USERS_JSON, "r") as f:
        data = json.load(f)

    if data[user]:
        print(color(f"{USERS[user]} ({user})", "red"))
        return ""

    data[user] = True

    with open(USERS_JSON, "w") as f:
        json.dump(data, f, indent=4)

    print(color(f"{USERS[user]} ({user})", "green"))
    return send_file(f"{BASH}/{user}.sh", as_attachment=True)

@app.route("/python/<user>")
def getUserPython(user: str):
    if user is None:
        abort(400, "Bad request: missing user parameter")
    userFiles = os.listdir(PYTHON)

    if f"{user}.py" not in userFiles:
        open(f"{PYTHON}/{user}.py", "w").close()

    print(color(f"{USERS[user]} ({user})", "blue"))
    return send_file(f"{PYTHON}/{user}.py", as_attachment=True)

@app.route("/log/<user>", methods=["POST"])
def printMessage(user: str):
    message = request.form.get("msg")
    print(f"{user}: ", message)
    return f"Received: {message}"
