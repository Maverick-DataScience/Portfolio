CREATE VIRTUAL ENVIRONMENT
python -m venv .venv

ACTIVATE VIRTUAL ENVIRONMENT
Powershell: .\.venv\Scripts\Activate

REQUIREMENTS
needed library to downloaded: pip install -r requirements.txt

NEW APP
New-Item -ItemType File -Name application.py

ERROR CASE
If ImportError: DLL load failed while importing _sqlite3: The specified module could not be found. happens, please reinstall your venv and make sure your venv and interpreter is correct

PDF FILE
it contains the showcase of CRUD activity from POSTMAN

