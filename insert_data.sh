#!/bin/bash

#psql command to connect to my database
PSQL="psql --username=sam --dbname=longview -t --no-align -c"
#getting output from payroll python script
OUTPUT=( $(python3 payroll_2023) )
#length of output
LEN=${#OUTPUT[@]}

#getting variables with correct labels
NAME=${OUTPUT[0]}
GROSS=${OUTPUT[1]}
SOCIAL=${OUTPUT[2]}
MED=${OUTPUT[3]}
STATE=${OUTPUT[4]}
FED=${OUTPUT[5]}
PAY=${OUTPUT[6]}

#inserting into mike with child_support, else every other insert
if [[ $NAME == 'mike' ]]
then 
    CHILD=58.20
    INSERT_INTO_DB=$($PSQL "INSERT INTO $NAME(gross, social, medicare, state, federal, net, child_support) VALUES($GROSS, $SOCIAL, $MED, $STATE, $FED, $PAY, $CHILD)")
else 
    INSERT_INTO_DB=$($PSQL "INSERT INTO $NAME(gross, social, medicare, state, federal, net) VALUES($GROSS, $SOCIAL, $MED, $STATE, $FED, $PAY)")

fi

#obtaining employee id by name
EMP_ID=$($PSQL "SELECT employee_id FROM employees WHERE name = '$NAME'")
EMP_ID_2023=$($PSQL "SELECT employee_id FROM year_2023 WHERE employee_id = $EMP_ID")

#function for adding values when updating in 2023
add() { n="$@"; bc <<< "${n// /+}"; }

#checking if employee id is in 2023
if [[ -z $EMP_ID_2023 ]]
then
    INITIAL_INSERT_2023=$($PSQL "INSERT INTO year_2023(employee_id, gross, net, federal, state, social, medicare) VALUES($EMP_ID, $GROSS, $PAY, $FED, $STATE, $SOCIAL, $MED)")
else
    GROSS_2023=$($PSQL "SELECT gross FROM year_2023 WHERE employee_id = $EMP_ID")
    NEW_GROSS=$(add $GROSS_2023 $GROSS)
    UPDATE_GROSS=$($PSQL "UPDATE year_2023 SET gross = $NEW_GROSS")
    NET_2023=$($PSQL "SELECT net FROM year_2023 WHERE employee_id = $EMP_ID")
    # NEW_NET=$(( $NET_2023 + $PAY ))
    NEW_NET=$(add $NET_2023 $PAY)
    UPDATE_NET=$($PSQL "UPDATE year_2023 SET net = $NEW_NET")
    FED_2023=$($PSQL "SELECT federal FROM year_2023 WHERE employee_id = $EMP_ID")
    # NEW_FED=$(( $FED_2023 + $FED ))
    NEW_FED=$(add $FED $FED_2023)
    UPDATE_FED=$($PSQL "UPDATE year_2023 SET federal = $NEW_FED")
    STATE_2023=$($PSQL "SELECT state FROM year_2023 WHERE employee_id = $EMP_ID")
    # NEW_STATE=$(( $STATE_2023 + $STATE ))
    NEW_STATE=$(add $STATE $STATE_2023)
    UPDATE_STATE=$($PSQL "UPDATE year_2023 SET state = $NEW_STATE")
    SOCIAL_2023=$($PSQL "SELECT social FROM year_2023 WHERE employee_id = $EMP_ID")
    # NEW_SOCIAL=$(( $SOCIAL_2023 + $SOCIAL ))
    NEW_SOCIAL=$(add $SOCIAL $SOCIAL_2023)
    UPDATE_SOCIAL=$($PSQL "UPDATE year_2023 SET social = $NEW_SOCIAL")
    MED_2023=$($PSQL "SELECT medicare FROM year_2023 WHERE employee_id = $EMP_ID")
    # NEW_MED=$(( $MED_2023 + $MED ))
    NEW_MED=$(add $MED $MED_2023)
    UPDATE_MED=$($PSQL "UPDATE year_2023 SET medicare = $NEW_MED")
fi