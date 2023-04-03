# def main():
#     print("Hello World")
    



# if __name__ == '__main__': 
    
#     main()
#     # why is this needed?
# IN python every class inherits from object class
# python has a facility called duck typing. 

class MyFirstClass:
    def __init__(self, x,y): #we can use any name instead of self
        self.name = y
        self.age = x
    def print_name(self):
        print(self.name) 
    def __contains__(self, x):
        if x == self.name:
            return True
        return False   
        
def main():
       f=MyFirstClass(10, "hello")
       f.print_name()
    
if __name__ == '__main__':
    main()
    
#     # print(f.name) india is my country all indians are my brothers and sistere 
    