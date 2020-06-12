from converters import mul, sum
# from ./packages.child import Child
# import converters

def performOprations(type, value1, value2):
    if(type.lower() == "sum"):
        result = sum(value1, value2)
        print("Ans is ", result)
    elif(type.lower() == "mul"):
        result = mul(value1, value2)
        print("Ans is ", result)
    else:
        print('Sorry, this type is not supported !!! ')

try:
    operationType = input("Enter opration type: ")
    value1 = int(input("Enter value 1: "))
    value2 = int(input("Enter value 2: "))
    performOprations(operationType, value1, value2)
except ValueError:
    print('Please enter valid value...')