# Make Python VirtualEnv and activate it
python -m venv venv
.\venv\Scripts\Activate.ps1

# Make sure PIP is the latest
python -m pip install --upgrade pip

# Install the Win32 Python API
pip install pywin32

# Install PyImGUI
pip install imgui[full]

