# !/bin/bash
set -x
source $(dirname $0)/secrets.sh
node --version
node test_alerts.js
