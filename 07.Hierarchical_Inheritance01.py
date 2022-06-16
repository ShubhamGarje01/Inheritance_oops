# when multiple child classes have one parent class then its become Hierarchical Inheritance

class Father:
    def showF(self):
        print("Father Class Instance Method")


class Son(Father):
    def showS(self):
        print("Son Class Instance Method")


class Girl(Father):
    def showG(self):
        print("Girl Class Instance Method")


s = Son()  # there is no constructor so, nothing will run while creating object
s.showS()  # show son
s.showF()  # show Father (because father inherited in Son and Girl)
g = Girl()
g.showG()  # Show girl
g.showF()  # show Father in girl class using girl class object
