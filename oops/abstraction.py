# Abstraction is to represent the essential features without representing explanation or background details.
# Main advantage is data hiding
# Abstraction is used to hide the internal functionality of the function.An abstraction is used to hide the
# irrelevant data or class inorder to reduce the complexity.
# A class that consists of one or more abstract method is called the abstract class
# Abstract method do not contain their implementations
# abstract class can be inherited by the subclass and abstract method gets its definition in the subclass
# abc module is used to do abstraction
# We cannot create object for abstract class. We can inherit the abstract class and we can declare
# the function on derived class. We can create object for the derived class
# if we don't provide definition to a method,it automatically becomes the abstract method

# class A:
#     def display(self):  #Function defnition  (With statements inside the function)
#         print("Hiiii")
#     def disp(self):     #function declaration (Without statements inside the function) - Abstract method
#         pass
# ob=A()
# ob.disp()
# ob.display()

# # Abstract class
# from abc import ABC,abstractmethod
# #abstract class
# class polygun(ABC):
#
#     #abstract method
#     @abstractmethod
#     def sides(self):
#         pass
#     def display(self):
#         print("Non abstract method")
# class Triangle(polygun):
#     def sides(self):
#         print("Triangle has 3 sides")
#
# t=Triangle()
# t.display()
# t.sides()