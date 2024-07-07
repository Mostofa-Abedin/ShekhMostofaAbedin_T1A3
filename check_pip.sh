#!/bin/bash

# T his function checks if pip package manger is installed.

# Check if pip3 is installed.
if ! command -v pip3 &> /dev/null; then
    # if not tell the user to install it by:
    echo "pip3 is not installed. Please install pip3. For most systems, you can install it by running 'sudo apt-get install python3-pip'."
    # Exit the script with status 1 (indicating an error)
    exit 1
fi
