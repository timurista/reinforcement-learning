# makes a box with linux

variable "tags" {
    type = map
    default = {
        Name = "AlpacaTradingRLApp"
    }
}

data "aws_ami" "hvm" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-2.0.20200917.0-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["amazon"]
}

# ami-0518bb0e75d3619ca
# Request a spot instance at $0.03
resource "aws_spot_instance_request" "traderapp" {
  ami           = "ami-0518bb0e75d3619ca"
  instance_type = "t2.small"
  iam_instance_profile="AWSSSMQuickAccess"
  subnet_id = "subnet-5de10f3a"
  
  tags = {
    Name = "CheapWorkerRequest"
  }

  wait_for_fulfillment = true
}

###########################
# spot instance hacks
###########################

data "aws_instance" "traderapp" {
  instance_id = aws_spot_instance_request.traderapp.spot_instance_id

  depends_on = [
    aws_spot_instance_request.traderapp,
  ]
}

resource "aws_ec2_tag" "traderapp_tags" {
  resource_id = data.aws_instance.traderapp.id
  # HACK, spots dont propogate tags
  # because instance is not there yet, got to wait for it then apply tags
  for_each = var.tags
  key         = each.key
  value       = each.value


  depends_on = [
    aws_spot_instance_request.traderapp,
  ]
}


output "instance_id" {
    value = aws_spot_instance_request.traderapp.spot_instance_id
}
