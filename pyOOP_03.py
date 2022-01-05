# import mypackage.pyOOP_01

from mypackage.pyOOP_01 import Class01, Class02

# import mypackage.subpackage.subpackage as subp

from mypackage.subpackage.subpackage import subPackClass

def main():
    # mypackage.pyOOP_01.main()

    o1= Class01()
    o2 = Class02()
    sub = subPackClass()

if __name__ == "__main__":
    main()