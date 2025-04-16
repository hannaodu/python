#list of EC2 instance
instance_ids = ["i-1234", "i=2134"]



#list of IP address for a security group 
ip_addresses = ["10.0.0.1","10.0.0.2","10.0.0.3"]



#list of availability zones in a region

availability_zones = ["eu-west-1a","eu-west-2b"]



#print the lists

print(f"EC2 instance to terminate: {instance_ids}")
print(f"IP addresses to allow: {ip_addresses}")
print(f"Availability zones: {availability_zones}")

#removing item from list and adding

#add new instance ID
instance_ids.append("i-5678")
print(f"Afer adding a new instace ID")
print(f"EC2 instance:", instance_ids)


#remove the first instance from the list
instance_ids.remove("i-1234")
print("After removing an instance")
print(f"EC2 instance:", instance_ids)

#check if an item is in a list
if "10.0.0.4" in ip_addresses:
    print("10.0.0.1 is is in and allowed")
else:
    print("10.0.0.4 is not in the list")
print("ip addresses:", ip_addresses)






