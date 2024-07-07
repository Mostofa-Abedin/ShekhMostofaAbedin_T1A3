#!/bin/bash

# This function check if a virtual environment exists. 

# Check if the virtualenv module is installed
if ! python3 -m venv --help &> /dev/null; then
    # If not tell the user to install it by:
    echo "virtualenv module is not installed. Please install it using 'pip3 install virtualenv' and try again."
    # Exit the script with status 1 (indicating an error)
    exit 1
fi
