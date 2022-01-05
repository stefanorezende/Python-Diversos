# a = 5

# print(type(a))
# print(a.__doc__)
# print(print.__doc__)

class Point:
    """This class represent the data-structure Point
    This is an example of multiline docstring...
    """
    
# print(p1.__doc__)
# print(help(p1))

    def __init__(self,x,y,z):
        '''The inicializer ---
        This inicializes the object with the passed arguments'''
        self.assign(x,y,z)

    def assign (self, x, y, z):
        'This assign the value to co-ordinates.'
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        'This prints the values of co-ordinates.'
        print (self.x,self.y,self.z)

# p1 = Point(1,2,3)
# p1.printPoint()

class Class01:
    def __init__(self):
        print ("Just create an object for Class01...")

class Class02:
    def __init__(self):
        print ("Just create an object for Class02...")

def main():
    o1 = Class01()
    o2 = Class02()

    print("breakpoint")


if __name__ == "__main__":
    print("Module pyOOP_01 is being run directly...")
    main()
    
else:
    print("Module pyOOP_01 has been imported in current Module")

