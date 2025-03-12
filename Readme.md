# Porsche HACCP Export to Rieber

## Overview

This [Windows Service using Python](https://metallapan.se/post/windows-service-pywin32-pyinstaller) grabs the menu plan data via trigger and exports it to Rieber's Check HACCP.

## Getting started and building

```cmd
# Create venv:
python -m venv .venv

# Activate venv:
.\.venv\Scripts\activate

# Upgrade pip
python.exe -m pip install --upgrade pip

# Prerequisites:
pip install -r requirements.txt
```