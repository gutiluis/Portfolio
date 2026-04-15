#!/bin/bash

# script to enforce python version for dependency vulnerability fix

chmod +x setup.sh
#set -e # why set -e?

# skip the installation if the version appears to be installed already
pyenv install -s 3.11.9
pyenv local 3.11.9

# multidimensional arrays
# An individual array element is accessed using an address called an index or subscript
# using data structure arrays. opposite to scalar variables. see bash
VENV=(python3 -m venv venv)
echo "[INFO] Creating virtual environment: ${VENV[*]}..."
"${VENV[@]}"

echo "[INFO] Activating environment..."
source venv/bin/activate

echo "[INFO] Installing dependencies..."
pip install -r requirements.txt

echo "[INFO] Setup complete."
