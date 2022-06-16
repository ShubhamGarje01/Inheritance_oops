# when a class inherits the features of more than one derived class or child class  that called as
# Multi-Level Inheritance.
class Father:
    def showF(self):
        print("Father Class Method")


class Son(Father):
    def showS(self):
        print("Son Class Method")


class GrandSon(Son):
    def showG(self):
        print("Grand Child Method")


obj = GrandSon()
obj.showF()
obj.showS()
obj.showG()

# to learn the execution use debug mode
