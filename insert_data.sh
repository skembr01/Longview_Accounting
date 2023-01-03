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

echo $PAY
echo $GROSS

# if [[ $NAME == 'mike' ]]
# then 
#     CHILD=58.20
#     INSERT_INTO_DB=$($PSQL "INSERT INTO $NAME(gross, social, medicare, state, federal, net, child_support) VALUES($GROSS, $SOCIAL, $MED, $STATE, $FED, $PAY, $CHILD)")
# else 
#     echo $NAME $GROSS $SOCIAL $MED $STATE $FED $PAY
# fi

# INSERT_INTO_DB=$($PSQL "INSERT INTO $NAME(gross, social, medicare, state, federal, net, child_support) VALUES($GROSS, $SOCIAL, $MED, $STATE, $FED, $PAY, $CHILD)")

