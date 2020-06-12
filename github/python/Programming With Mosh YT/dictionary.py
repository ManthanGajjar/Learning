
# like an object

user = {
    "1": "one",
    "2": "two",
    "3": "three"
}

number = input("Enter number: ")
string = ""
for i in number:
    string += " " + user.get(i, i);
print(string)

# print(user["name"])