# this program is for to check and learn how to access the constructor in child class.

class Father:  # Parent Class
    def __init__(self, ):  # Constructor of Parent class
        # self.money = m
        self.money = 2222
        print("this is constructor of Parent Class")

    def show(self):  # Instance Method of Parent Class
        print("this is Instance method of Parent Class: ", self.money)


class Son(Father):  # Child Class
    def disp(self):  # Instance Method of Child Class
        print("this is Instance method of Child Class", self.money)  # we can use constructor variable in child class
        print("this is Instance method of Child Class", self.money + 5000)


# s = Son(102030405)  # creating child class object -- this will give us the constructor as output
s = Son()  # creating object = executing the constructor

s.show()  # accessing instance method of Parent Class
s.disp()  # accessing instance method of Child Class
m = s.money  # accessing constructor variable
print(m)
s.money = 20220  # modifying constructor variable
s.show()  # CHECKING FOR MODIFIED VALUE

# we can pass argument with object also, for that we need to add extra variable in constructor parameters like (self, m)
# and then self.money = m and while creating the object pass that argument like s.Son(1231230)
