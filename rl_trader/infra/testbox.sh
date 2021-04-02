# !/bin/bash
set -x
export AWS_PROFILE=timurista-dev
export AWS_REGIOn=us-west-2
ID=$(aws ec2 describe-instances --filters 'Name=tag:Name,Values=AlpacaTradingRLApp' --output json | jq -r ".Reservations[0].Instances[0].InstanceId" )
echo $ID

aws ec2 start-instances --instance-ids $ID --output json | jq
count=0

aws ssm send-command \
        --document-name "AWS-RunShellScript" \
        --targets "Key=InstanceIds,Values=$ID" \
        --parameters '{"commands":["#!/bin/bash","cd ~","./hello"]}' | jq

while [ "$?" -ne "0" ]
do
    (( count ++))
    echo "attempt $count"
    if [ count -ge 10 ]
    then
        echo "giving up"
        exit
    fi
    sleep 10
    aws ssm send-command \
        --document-name "AWS-RunShellScript" \
        --targets "Key=InstanceIds,Values=$ID" \
        --parameters '{"commands":["#!/bin/bash","cd ~","./hello"]}' | jq
done

echo "stop box"

aws ec2 stop-instances --instance-ids $ID --output json | jq

echo "All done"
