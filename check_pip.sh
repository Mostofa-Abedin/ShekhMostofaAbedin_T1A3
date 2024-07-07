#!/bin/bash
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip3. For most systems, you can install it by running 'sudo apt-get install python3-pip'."
    exit 1
fi
