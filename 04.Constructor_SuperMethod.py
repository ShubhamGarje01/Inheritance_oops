# super method to access parent class constructor from child class
# if we go with argument, we need to add parameter in all constructors __init__ and in all methods
# where we call that variable and pass the argument while creating object and calling to variable methods
class Father:
    def __init__(self):
        self.money = 100
        print("Parent Class Constructor")

    def show(self):
        print("Instance Method of Parent Class")


class Son(Father):
    def __init__(self):
        super().__init__()  # super method (to access parent class constructor)
        self.var = 'Yes'
        print("is this child class constructor ?  --> ", self.var)

    def disp(self):
        print("Instance Method of child class: ", self.money)  # accessing Parent class constructor
        print("Instance Method of child class: ", self.var)  # accessing child class constructor


s = Son()
s.disp()
s.show()
