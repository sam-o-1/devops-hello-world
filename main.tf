resource "aws_s3_bucket" "devops_lab_bucket" {
  bucket = "soham-devops-project-bucket"

  tags = {
    Name        = "My Local Bucket"
    Environment = "Dev"
  }
}

