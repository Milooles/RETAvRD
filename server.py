from flask import Flask, abort, send_file
import os

app = Flask(__name__)

# ?user=011935
@app.route("/<user>")
def getUser(user: str = None):
    if user is None:
        abort(400, "Bad request: missing user parameter")
    userFiles = os.listdir("./users")
    if f"{user}.sh" not in userFiles:
        open(f"./users/{user}.sh", "w").close()
    return send_file(f"./users/{user}.sh", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
