#!/bin/bash
DOUBLE=0
TRIPPLE=0

while read line; do
    hastwo=0
    hasthree=0
    origline=$line
    while [ "${#line}" -ne "0" ]; do
       len=${#line}
       char=${line:0:1}
       line=${line//$char}
       if [ "$(($len - ${#line}))" -eq "2" ] && [ "$hastwo" -eq "0" ]; then
           hastwo=1
       fi
       if [ "$(($len - ${#line}))" -eq "3" ] && [ "$hasthree" -eq "0" ]; then
           hasthree=1
       fi
       # Don't bother searching further if both are found
       if [ "$hastwo" -eq "1" ] && [ "$hasthree" -eq "1" ]; then
           break
       fi
    done
    DOUBLE=$(($DOUBLE+$hastwo))
    TRIPPLE=$(($TRIPPLE+$hasthree))
done < input.txt
echo $(($DOUBLE*$TRIPPLE))
