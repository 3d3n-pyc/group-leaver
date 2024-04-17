REM Installer les dépendances
python -m pip uninstall -y -r interferances.txt
python -m pip install -y -r requirements.txt

REM Lancer le programme
python main.py