# !/bin/bash

# DATA=$(cat .data/)
# if [-z "$DATA"]; then
#     wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/aapl_msi_sbux.csv
# fi

source .venv/bin/activate
# train
python rl_trader.py -m train
# test
python rl_trader.py -m test
