#!/bin/bash

# This script runs the main program .

# All external functions are imported. 
# Function to check if python exists on Local machine.
source check_python.sh
# Function to check if pip package manager exists on Local machine.
source check_pip.sh
# Function to check if virtual environment exists on Local machine.
source check_virtualenv.sh
# Function: If virtual environment doesn't exist, setup virtual environment. 
source setup_virtualenv.sh
# Function: Install packages from requirement.txt. I nthis case requirements.txt is empty.
source install_packages.sh

# Run the main program.
python3 src/main.py
# Let user know application is running.
echo "Application running."
# Deactivate virtual environment at the end.
source deactivate_virtualenv.sh
