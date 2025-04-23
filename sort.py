#Sorting a list -uselful for organizing resources in a sepcific order
#list of EC2 instance
instance_ids = [ "i-2314", "i-2134" ,"i-1234"]


print(f"EC2 instance to terminate: {instance_ids}")

# Sorting
instance_ids.sort()
print(f"EC2 instance sorted: {instance_ids}")


