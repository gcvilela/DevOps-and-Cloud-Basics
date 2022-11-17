variable "access_key" {
  default = ""
}

variable "secret_key" {
  default = ""
}

variable "region" {
  default = "us-east-1"
}

variable "zone" {
  default = "us-east-1d"
}

variable "pk" {
  default = ""
}

variable "ec2_name" {
  default = "jt-marianadmoreira-terraform"
}

variable "bucket_name" {
  default = "jt-marianadmoreira-terraform"
}

variable "owner" {
  default = "Mariana Moreira"
}

variable "secg" {
  default = "sg-0249eaf2a087690c7"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami_linux" {
  default = {
     "us-east-1" = "ami-0b898040803850657"
   }
}


