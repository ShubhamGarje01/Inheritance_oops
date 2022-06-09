# Single Inheritance:- If a single child class is derived from parent class, its called as Single Inheritance.
# and how to access parent class using child class

class Father:  # (object) is optional  ## Parent Class
    money = "1 CR"

    def show(self):  # Instance Method
        print("Instance method of Parent class")

    @classmethod
    def showMoney(cls):  # Class Method
        print("Class method of Parent class: ", cls.money)

    @staticmethod
    def statMethod():  # Static Method
        var = 10010110
        print("Static Method of Parent Class: ", var)


class Son(Father):  # Child Class
    def disp(self):  # Instance Method of child class
        print("Instance method of Child Class")


s = Son()  # creating object of child class
s.disp()  # accessing instance method of Child class
s.show()  # accessing instance method of Parent class
s.showMoney()  # accessing class method of Parent class
s.statMethod()  # accessing static method of Parent class
print(s.money)  # accessing Parent class variable
m = s.money   # accessing Parent class variable using new variable
print(m)
n = s.money = "2 CR"  # modifying Parent class variable
print(n)

# we can access father class separately too

f = Father()  # creating object of father class
f.show()
f.showMoney()

# we can not access child class method using father class or father class object,