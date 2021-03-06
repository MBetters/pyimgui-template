# Make Python VirtualEnv and activate it
python -m venv venv
.\venv\Scripts\Activate.ps1

# Make sure PIP is the latest
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
