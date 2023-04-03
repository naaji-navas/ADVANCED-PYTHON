class FirstClass:
    def __init__(self, x, y) -> None:
        self.first = x
        self.second = y

    def __contains__(self, x):
        if x == self.first or x == self.second:
            return True
        return False

    def __add__(self, s):
        temp = FirstClass(0, 0)
        temp.first = self.first + s.first
        temp.second = self.second + s.second
        return temp
    def display(self):
        print(self.first, self.second)
    def world(self):
        print("hello world")


if __name__ == "main":
    f = FirstClass(10, 20)
    g = FirstClass(30, 40)
    
    
    h = f + g
    h.display()
    
    #name mangling in python is used to avoid name clashes in python
    # __name__ is a special variable in python
    # __name__ is a special variable in python
