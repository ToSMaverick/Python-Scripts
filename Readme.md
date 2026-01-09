# Useful Python Scripts

## Overview

This Repo contains a few useful scripts that I needed at some point.

## Scripts

### move-mouse.py
Prevents the computer from going to sleep or locking the screen by slightly moving the mouse cursor every 30 seconds.

### MergePDFs.py
Merges all PDF files in the current directory into a single file named `Merged_pdfs.pdf`. It supports handling password-protected PDFs by prompting the user for a password.

## Getting started

```cmd
# Create venv
uv venv

# Activate venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Prerequisites
uv pip install -r requirements.txt

# Build a certain script
uv run pyinstaller --onefile --runtime-tmpdir=. --hidden-import win32timezone myservice.py
```
