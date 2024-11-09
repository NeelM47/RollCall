#!/bin/bash

echo "Is environment running ???"

echo "Starting server ..."

sudo systemctl start mongod

clear
# Prompt the user for input
echo "Do you want to proceed with generating attendance file? (y/n)"
read user_input

# Check the user's input
if [ "$user_input" == "y" ]; then
    # Run the next commands only if the input is "yes"
    echo "Proceeding with the next steps..."

    # Command 1 (e.g., node server)
	mongoexport --db mydatabase --collection datas --out data/data.json --jsonArray

    # Command 2 (e.g., mongoexport)
    python3 attendance.py

else
    echo "You chose not to proceed. Exiting script."
    exit 0
fi
