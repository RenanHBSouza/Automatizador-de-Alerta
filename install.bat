@echo off
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install -r Source/requirements.txt
start /b python main.py
pause