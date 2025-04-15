#concatenate

#define aws ID 
accound_id = "123456678"

#project name

project_name = "aws-automation"

#concatenate strings to form the s3 bucket name

bucket_name = accound_id + "-" + project_name + "-bucket"

#print result 
print(f"S3 Bucket Name: {bucket_name}")

#string formatting
print("S3 Bucket Name: {}".format(bucket_name))

print(f"S3 Bucket Name: {bucket_name}")

#Environmnet name
environment_name = "dev" #development

#application name
application_name = "webapp" #web application

#instance number
instance_number = 1 #first instance

#concatenate

instance_name = f"{environment_name}-{application_name}-{instance_number}"


#print result
print(f"Instance Name: {instance_name}")



