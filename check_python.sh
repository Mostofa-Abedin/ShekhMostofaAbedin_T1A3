#!/bin/bash
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3 from https://www.python.org/downloads/ and try again."
    exit 1
fi
