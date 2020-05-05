# Goal - Perform linear search -> Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

# Input : arr[] = [10,20,30,40,60,50,110,100,130,170]
# x = 60;
# Output : 4

def main(args, searchElement):
    for i in args:
        if(i == searchElement):
            # to get index of nth element in array use array.index(nth element)
            return args.index(i)
    return 'not found'

inputs = [10,20,30,40,60,50,110,100,130,170]
searchElement = 60
result = main(inputs, searchElement)
print(result)
