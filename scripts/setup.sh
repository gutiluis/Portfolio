#!/bin/bash

# setup script to install requirements.txt, update pip, fix vulnerabilities
# script to enforce python version for dependency vulnerability fix

echo "[INFO] run chmod"
chmod +x setup.sh
echo "[INFO] prevent run after a false boolean... and exit immediately the script"
set -e # why set -e?

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

echo "[INFO] upgrade pip and setuptool and wheel.. entire packaging toolchain. both not under requirements.txt"
# upgrade pip and setuptools
pip install --upgrade pip setuptools wheel

echo "[INFO] Installing dependencies..."
pip install -r requirements.txt

echo "[INFO] Installing dev-requirements..."
pip install -r dev-requirements.txt"


echo "[INFO] Setup complete."
