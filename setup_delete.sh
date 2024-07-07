#!/bin/bash

# Function to check if Python is installed.
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo "Python3 is not installed. Please install Python3 from https://www.python.org/downloads/ and try again."
        exit 1
    fi
}

# Function to check if pip package manager is installed.
check_pip() {
    if ! command -v pip3 &> /dev/null; then
        echo "pip3 is not installed. Please install pip3. For most systems, you can install it by running 'sudo apt-get install python3-pip'."
        exit 1
    fi
}

# Function to check if virtualenv is installed.
check_virtualenv() {
    if ! python3 -m venv --help &> /dev/null; then
        echo "virtualenv module is not installed. Please install it using 'pip3 install virtualenv' and try again."
        exit 1
    fi
}

# Function to create and activate virtual environment.
setup_virtualenv() {
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        echo "Virtual environment created."
    else
        echo "Virtual environment already exists."
    fi
    source venv/bin/activate
    echo "Virtual environment activated."
}

# Function to install required packages
install_packages() {
    pip install -r requirements.txt
    echo "Required packages installed."
}

# Function to deactivate virtual environment
deactivate_virtualenv() {
    deactivate
    echo "Virtual environment deactivated."
}
