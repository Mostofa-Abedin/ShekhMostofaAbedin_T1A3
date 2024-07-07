#!/bin/bash
if ! python3 -m venv --help &> /dev/null; then
    echo "virtualenv module is not installed. Please install it using 'pip3 install virtualenv' and try again."
    exit 1
fi
