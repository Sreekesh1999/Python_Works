# Constructors are the member functions of a class which will automatically executted when an
# object of a class is created
# constructors do not have return value
# we can define a constructor by using below syntax def __init__(self):
# class A:
#     def __init__(self):
# ob=A()
# Mainly 2 types of constructors
#     non parameterized constructor
#     parameterized conductor

# #Non parameterized constructor(default constructor)
# class A:
#     def __init__(self):
#         print("Non parameterized constructor")
# obj=A()

# #parameterized conductor
# class A:
#     def __init__(self,name):
#         print("parameterized constructor")
#         self.a=name
#     def display(self):
#         print("Name is :",self.a)
# ob=A("Sree")
# ob.display()

#distructor - Used to remove object
class A:
    def __init__(self,name):
        print("constructor")
        self.na=name
    def __del__(self):
        print("Distructor")
    def display(self):
        print("Name is :",self.na)
ob=A("sreekeh")
del ob
ob.display()






