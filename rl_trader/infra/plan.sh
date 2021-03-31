# !/bin/bash
HERE=$(dirname $0)
source $HERE/secrets.sh

tf init
tf plan
