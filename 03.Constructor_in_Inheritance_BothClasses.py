# this program is to check what happen if parent class and child class both have their own constructors?
# which one will get executes?


class Father:
    def __init__(self):
        self.money = 1000
        print("this is Parent Class Constructor: ", self.money)

    def show(self):
        print("Parent Class Instance Method")


class Son(Father):
    def __init__(self):
        self.money2 = 2000
        print("Child Class Constructor: ", self.money2)

    def disp(self):
        print("Chile Class Instance Method")


s = Son()  # this object executes child class constructor
s.show()  # we can access the methods# of parent class
s.disp()  # we can access the methods of child class but not constructor
print(s.money2)  # accessing variable of child class constructor
# print(s.money)  # accessing variable from parent constructor ERROR
# we can not access the father class constructor if both classes have their own constructor, or we can say that
# child class constructor gets replace with parent constructor because of inheritance
f = Father()
print(f.money)
