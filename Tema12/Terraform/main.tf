provider "aws" {
  access_key = var.access_key 
  secret_key = var.secret_key 
  region = var.region
  version = "~> 4.1"
  
}

resource "aws_key_pair" "key_pair" {
  key_name = "ec2_key_pair"
  public_key = var.pk
}

resource "aws_s3_bucket" "b" {
  bucket = var.bucket_name 
  acl = "private"
}

resource "aws_s3_bucket_object" "objects" {
  for_each = fileset("../Scripts/", "**")
  bucket = aws_s3_bucket.b.id
  key = each.value
  source = "../Scripts/${each.value}"
  etag = filemd5("../Scripts/${each.value}")
  
}

resource "aws_instance" "docker_python_ec2" {
  count = 1
  depends_on = [ aws_key_pair.key_pair ]
  availability_zone = var.zone
  vpc_security_group_ids = [ var.secg ]
  ami = lookup(var.ami_linux,var.region)
  instance_type = var.instance_type
  key_name = aws_key_pair.key_pair.key_name
  user_data = file("run.sh")

  tags = {
    "Name" = var.ec2_name
    "EC2_ECONOMIZATOR" = "TRUE"
    "Project" =	"ILEGRA-JT-DEVOPSCLOUD"
    "Owner" = var.owner
    "CustomerID" = "ILEGRA-JTS"
  }
}
