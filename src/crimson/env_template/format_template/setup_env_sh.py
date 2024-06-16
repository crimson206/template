templates = {}

templates['base'] = r'''\[bin_bash\]

read -p "Please enter the Python version you want to use (e.g., 3.9): " PYTHON_VERSION

conda create --name \[module_name\] python=$PYTHON_VERSION -y

conda activate \[module_name\]

pip install -r requirements.txt

'''
