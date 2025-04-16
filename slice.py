#slicing a List-it alllows us to get a portoin of a list 

#availability zones
availability_zones = ["eu-west-1a","eu-west-2b","eu-west-3c","eu-west-4d"]
print(f"Number of AZs:{availability_zones}")

#slicing the list
#first two AZ
first_two_azs = availability_zones[:2]
print(f"First two AZs: {first_two_azs}")


