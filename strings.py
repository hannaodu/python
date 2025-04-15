

#single quotes for aws region
aws_region = "eu-west-2"

#double quotes string for an instance type 
instance_type = "t2.micro"

#triple quotes string for a IAM policy
iam_policy = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}"""

#print variables
print(aws_region)
print(instance_type)
print(iam_policy)





