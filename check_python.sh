#!/bin/bash

# This function checks if python3 is installed.

# Check if Python3 is installed.
if ! command -v python3 &> /dev/null; then
    # If not, tell the user to install it by:
    echo "Python3 is not installed. Please install Python3 from https://www.python.org/downloads/ and try again."
    # Exit the script with status 1 (indicating an error).
    exit 1
fi
