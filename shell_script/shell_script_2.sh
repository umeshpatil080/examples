#!/usr/bin/bash

START=$(date +%s)
sleep 2
END=$(date +%s)
DIFF=$(( $END - $START ))

if [ "$DIFF" -gt 1 ]
then
    echo "It took $DIFF seconds"
else
    echo "No need to check"
fi