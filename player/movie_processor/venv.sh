# !/bin/bash

virtualenv -p python3.8 .venv
source .venv/bin/activate
which python
which pip
# only use 3.8 for tensorflow
pip install -r requirements.txt
