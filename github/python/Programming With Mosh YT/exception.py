# learn how to handle errors in PY

try:
    # what if we enter string instand of integer
    number = int(input("Enter number: "))
    print(number)
except ValueError:
    print('Invalid value..')