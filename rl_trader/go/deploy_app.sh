# !/bin/bash
# go get -u github.com/mholt/caddy

# PATH=$(which caddy)
env GOOS=linux GOARCH=amd64 go build hello.go
# binary=$(mktemp)
# mv hello binary 
# go run hello.go
export AWS_PROFILE=timurista-dev
export AWS_REGION=us-west-2
aws s3 ls s3://timurista-gofiles

if [ $? -ne 0 ]; then
    echo "make bucket"
    aws s3 mb s3://timurista-gofiles
fi

aws s3 cp hello s3://timurista-gofiles/ --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers
