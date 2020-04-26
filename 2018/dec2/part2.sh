#!/bin/bash
words=""
while read line; do
    value=0
    iter=0
    origline=$line
    while [ "${#line}" -ne "0" ]; do
       len=${#line}
       char=${line:0:1}
       line=${line//$char}
       char_value=$(printf "%d" "'$char")
       char_count=$(($len-${#line}))
       value=$(($value+$char_count*$char_value))
    done
    words="$words$value:$origline "
done < input.txt

echo $words | tr " " "\n" | sort
