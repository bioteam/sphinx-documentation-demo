#!/bin/sh
if [ -d ".env" ]; then
  source .env/bin/activate
else
  # If environment doesn't exist, install it
  python -m venv .env
  source .env/bin/activate
  python -m pip install -e .
fi
