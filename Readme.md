# Useful Python Scripts

## Overview

This Repo contains a few useful scripts that I needed at some point.

## Getting started

```cmd
# Create venv:
python -m venv .venv

# Activate venv:
.\.venv\Scripts\activate
source .venv/bin/activate

# Upgrade pip
python.exe -m pip install --upgrade pip

# Prerequisites:
pip install -r requirements.txt

# Build a certain script
pyinstaller --onefile --runtime-tmpdir=. --hidden-import win32timezone myservice.py
```
