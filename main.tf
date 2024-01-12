provider "aws" {
  region = "us-east-1"  # Specify your desired AWS region
}

resource "aws_instance" "example" {
  ami           = "ami-079db87dc4c10ac91"  # Specify the AMI ID for your desired image
  instance_type = "t2.micro"                # Specify the instance type

  tags = {
    Name = "example-instance"
  }
}
