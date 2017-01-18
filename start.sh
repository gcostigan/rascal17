#!/bin/bash

# Start the xbox controller thread in the background to be called
xboxdrv --silent --detach-kernal-driver &

# Start the main script
python main.py

# Clean up and kill all background process
killall xboxdrv
