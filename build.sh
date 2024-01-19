#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Run any additional build commands
python app.py 
