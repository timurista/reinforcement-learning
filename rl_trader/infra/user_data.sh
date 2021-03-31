# !/bin/bash
cd ~
aws s3 cp s3://timurista-gofiles/hello hello
chmod +x hello

# TODO: use a proper linux service to run in bg
