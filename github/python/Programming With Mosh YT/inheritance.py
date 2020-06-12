#inheritance = do not repeat same line of code again and again
class reusableClass:
    def walk(self, type):
        print(f"{type} calling...")

# in parameter add class name which you're going to inherite
class dog(reusableClass):
    pass

class cow(reusableClass):
    pass



dog().walk("Dog")
cow().walk("Cow")
