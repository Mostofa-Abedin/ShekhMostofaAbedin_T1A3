#!/bin/bash

# This function sets up the virtual environment. 

# Check if the 'venv' directory (virtual environment) does not exist.
if [ ! -d "venv" ]; then
    # If it does not, create a venv.
    python3 -m venv venv
    echo "Virtual environment created."
else
    # Else inform user venv exists.
    echo "Virtual environment already exists."
fi
# # Activate the virtual environment and let the user know.
source venv/bin/activate
echo "Virtual environment activated."
