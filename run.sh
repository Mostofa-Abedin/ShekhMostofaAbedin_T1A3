#!/bin/bash

# Import functions from setup.sh
source setup.sh

# Run setup checks and operations
check_python
check_pip
check_virtualenv
setup_virtualenv
install_packages

# Run the main application
python src/main.py
echo "Application running."

# Deactivate virtual environment after running the application
deactivate_virtualenv
