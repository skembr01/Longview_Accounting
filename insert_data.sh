#!/bin/bash

PSQL="psql --username=sam --dbname=longview -t --no-align -c"

OUTPUT=( $(python3 payroll_2023) )
# echo $OUTPUT
# echo ${OUTPUT[1]}
# # NAME=${OUTPUT[0]}
# # echo $NAME
LEN=${#OUTPUT[@]}

NAME=${OUTPUT[0]}
# $OUTPUT | read NAME GROSS SOCIAL MED STATE FED PAY 
GROSS=${OUTPUT[1]}
SOCIAL=${OUTPUT[2]}
MED=${OUTPUT[3]}
STATE=${OUTPUT[4]}
FED=${OUTPUT[5]}
PAY=${OUTPUT[6]}

if [[ $NAME == 'mike' ]]
then 
    CHILD=58.20
    echo $NAME $GROSS $SOCIAL $MED $STATE $FED $CHILD $PAY
else 
    echo $NAME $GROSS $SOCIAL $MED $STATE $FED $PAY
fi