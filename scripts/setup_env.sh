#!/bin/bash

# If module name is NONE, let user read README.md first
if [ "$MODULE_NAME" = "NONE" ]; then
    echo "Please read the README.md first."
    exit 1
fi

read -p "Please enter the Python version you want to use (e.g., 3.9): " PYTHON_VERSION

conda create --name $MODULE_NAME python=$PYTHON_VERSION -y

conda activate $MODULE_NAME

pip install -r requirements.txt
