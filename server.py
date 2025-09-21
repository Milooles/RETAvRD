import subprocess, time, requests, threading, logging, utils
from flaskServer import getApp, USERS

def run_ngrok():
    ngrok = subprocess.Popen(
        ["ngrok", "http", "8000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(5)

    url = "http://localhost:4040/api/tunnels"
    publicURL = requests.get(url).json()["tunnels"][0]["public_url"]
    print(publicURL)

    # update firebase
    r = requests.put("https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/.json", json={"IP": publicURL})
    r.raise_for_status()
    return ngrok
def run_flask():
    getApp().run(host="0.0.0.0", port=8000, debug=False)

flaskThread = threading.Thread(target=run_flask, daemon=True)
flaskThread.start()

flaskLog = logging.getLogger('werkzeug')
flaskLog.setLevel(logging.ERROR)

ngrok = run_ngrok()

while True:
    user = input("")
    if user in USERS.keys():
        utils.modifyUser(user)
