#!/bin/bash

# Start the Node.js server in the background
#node src/index.js &

# Capture the process ID (PID) of the Node.js server so we can stop it later
#SERVER_PID=$!

# wait a moment for the server to initialize (optional)
#sleep 5

# now you can proceed with the next commands, even while the server is running

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
