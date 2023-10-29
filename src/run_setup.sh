#!/bin/bash
echo "Starting setup for Horse Stable Management App..."

#Creating virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required python packages 
echo "Installing required packages..."
python3 -m pip install -r requirements.txt
echo "Setup completed successfully!"

echo "To run the app, please enter the following: bash run_app.sh"