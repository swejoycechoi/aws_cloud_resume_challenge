terraform {
    required_providers {
        aws = {
            version = "~> 4.0" 
            source = "hashicorp/aws"
        }
    }
}
provider "aws" {
    profile = "710271919598_PowerUserAccess" # aws cli profile
    region = "us-west-1"
}