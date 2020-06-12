# importing one of the package module and calling it
from packages.child import Child
Child()

names = ["X", "Y", "Z", "A", "B", "C"]

# gives result from index 3 to the end
print(names[3:])

# gives result from end to start
print(names[-3])


# gives result from index 3 to 4, we didn't get last index value in the array
print(names[3:4])

# check any field exist or not in the list, return bool

print ("DD" in names)