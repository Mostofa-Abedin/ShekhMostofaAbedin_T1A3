#!/bin/bash
# This function installs the required external packages from requirements.txt

# Read requirements.txt and install the packages.
pip install -r requirements.txt
# Let user know packages have been installed.
echo "Required packages installed."
