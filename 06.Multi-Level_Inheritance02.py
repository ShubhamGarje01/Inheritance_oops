# when a class inherits the features of more than one derived class or child class  that called as
# Multi-Level Inheritance.
class Father:
    def __init__(self):
        print("Father Constructor")

    def showF(self):
        print("Father Class Method")


class Son(Father):
    def __init__(self):
        super().__init__()  # calling Father constructor in Son class
        print("Son Constructor")

    def showS(self):
        print("Son Class Method")


class GrandSon(Son):
    def __init__(self):
        super().__init__()  # calling Son Constructor in Grandson class
        print("Grand Son Constructor")

    def showG(self):
        print("Grand Child Method")


obj = GrandSon()  # this will print Grand Son Constructor only
# we can use all class methods but can use only one constructor
# class get execute ust by creating object so, all constructor will get executed when we create object if we use
# super() method.
# obj.showF()
# obj.showS()
# obj.showG()

# we will use super() method to call all constructor
# to learn the execution use debug mode
