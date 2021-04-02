# !/bin/bash
set -x
export AWS_PROFILE=timurista-dev
export AWS_REGIOn=us-west-2
ID=$(aws ec2 describe-instances --filters 'Name=tag:Name,Values=AlpacaTradingRLApp' --output json | jq -r ".Reservations[0].Instances[0].InstanceId" )
echo $ID

aws ec2 start-instances --instance-ids $ID --output json | jq

count=1

aws ssm start-session --target $ID

while [ "$?" -ne "0" ]
do
    (( count ++))
    echo "attempt $count"
    sleep 10
    aws ssm start-session --target $ID
done

echo "All done"
