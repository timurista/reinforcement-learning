provider "aws" {
  region  = "us-west-2"
  profile = "timurista-dev"
}

terraform {
  backend "s3" {
    bucket = "timurista-tfstate-us-west-2"
    key    = "alpaca_trader/rl_trader.tfstate"
    region = "us-west-2"
  }
}
# a box to deploy things

provider "local" {}
