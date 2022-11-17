cd "path\folder-venv"
folder-venv\activate.bat
cd "path\Scripts"
python main.py
aws s3 sync "path\Scripts" "s3://path/Scripts/"
