# it's like list, but we can not change the value, it's immutable


numbers = (1,2,3)

# print(numbers[0])

# unpacking
# to get any value from tuple or list we can do this

value1 = numbers[0]
value2 = numbers[1]

# like this but we can do unpacking to get all value like this

valueA, valueB, valueC = numbers

print(value1 , " " , valueA);