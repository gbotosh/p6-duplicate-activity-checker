@echo off
echo Creating virtual environment...

if not exist .venv (
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate

echo Installing required packages...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Creating folders...
if not exist data_raw mkdir data_raw
if not exist outputs mkdir outputs

echo Running duplicate checker...
python check_duplicates.py

pause