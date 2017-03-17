#!/bin/bash

# Initialize header file
cat startup_screen.txt

# Start the xbox controller thread in the background to be called
echo "Starting xbox controller instance..."
xboxdrv --silent --detach-kernal-driver &
echo "Done."

# Start the main script
echo "Starting main script..."
python main.py
echo "Done."

# Clean up and kill all background process
echo "Cleaning up processes..."
killall xboxdrv
echo "Shutting down."
