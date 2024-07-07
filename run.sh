#!/bin/bash
source check_python.sh
source check_pip.sh
source check_virtualenv.sh
source setup_virtualenv.sh
source install_packages.sh

python src/main.py
echo "Application running."

source deactivate_virtualenv.sh
