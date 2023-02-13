# polymorphism - Polymorphism refers to having multiple forms. Polymorphism is a programming
# term that refers to the use of the same function name, but with different signatures, for multiple types.
# One_In-Many Forms
# Two types -
#     1.compile Time (Eg:Function overloading)
#     2.Run Time  (Eg:Function overriding)
#
#
#
# Function overloading means one class have more than one functions with same function name and different
# signatures(number,order and type of parameters)
#
# Function overriding Different class have different functions with same function name and same signature

# python won't support function overloading directly.
# class A:
#     def sum(self,a):
#         print("sum is ",a+a)
#     def sum(self,a,b):
#         print("sum is ",a+b)
# ob=A()
# ob.sum(10)

# instead of function overloading we can use below method(using different parameters)
# class A:
#     def display(self,name=None):
#         if name is None:
#             print("Hello")
#         else:
#             print("Hello",name)
# ob=A()
# ob.display()
# ob.display("sreekesh")

class rectangle:
    def area(self,l,b):
        print("area of rectangle is",l*b)
class square(rectangle):
    def area(self,l,b):
        print("area of square is",l*b)
ob=square()
ob.area(10,20)

    #need to check difference between overloading and overriding
    # what is super functions - Syntax - example

