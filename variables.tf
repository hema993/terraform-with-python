variable "region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "ami" {
  # Amazon Linux 2 AMI - ap-south-1
  default = "ami-0305d3d91b9f22e84"
}

variable "key_name" {
  description = "Your AWS key pair name"
  type        = string
}

