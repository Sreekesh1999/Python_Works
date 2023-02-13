# oop concepts
# Encapsulation- wrapping up of data and function into a single unit..Eg Class
# inheritance - To aquaire the properties of one class to another class
# use -code reusability
# Types of inheritance
#       single inheritance
#       multi level inheritance  - intermediate class will be there
#       multiple inheritance  - Multiple base classes will be there
#       Hierarchical inheritance - one base and many derived
#       Hybrid inheritance - Combination of hierarchical and multiple

# #single inheritance
# class A:
#     def base(self):
#         print("Base class")
# class B(A):
#     def derived(self):
#         print("Derived class")
# obj=B()
# obj.base()
# obj.derived()

# #take input from user on first class. Inherit values to second class and find sum of the numbers (single inheritance )
# class A:
#     def read(self):
#         self.x=int(input("Enter your first number :"))
#         self.y=int(input("Enter your second number :"))
# class B(A):
#     def sum(self):
#         print("Sum is :",self.x+self.y)
# obj=B()
# obj.read()
# obj.sum()

# #Multi level inheritance
# class A:
#     def read(self):
#         self.x=int(input("Enter your first number :"))
#         self.y=int(input("Enter your second number :"))
# class B(A):
#     def sum(self):
#         self.s=self.x+self.y
#         print("Sum is :",self.s)
# class C(B):
#     def Avg(self):
#         print("Avg is ",self.s/2)
# obj=C()
# obj.read()
# obj.sum()
# obj.Avg()

# read two variable in Class A
#  Find sum in Class B
#  Find Avg in Class C
#  find product in Class D

# #Heirarchial inheritance
# class A:
#     def read(self):
#         self.x=int(input("Enter your first number :"))
#         self.y=int(input("Enter your second number :"))
# class B(A):
#     def sum(self):
#         self.s=self.x+self.y
#         print("Sum is :",self.s)
# class C(A):
#     def Avg(self):
#         print("Avg is ",(self.x+self.y)/2)
# class D(A):
#     def product(self):
#         print("product is ",self.x*self.y)
#
# ob1=B()
# ob1.read()
# ob1.sum()
#
# ob3=C()
# ob3.read()
# ob3.Avg()
#
# ob4=D()
# ob4.read()
# ob4.product()

# #Hybrid
# class A:
#     def read(self):
#         self.x=int(input("Enter your first number :"))
#         self.y=int(input("Enter your second number :"))
# class B(A):
#     def sum(self):
#         self.s=self.x+self.y
#         print("Sum is :",self.s)
# class C(A,B):
#     def Avg(self):
#         print("Avg is ",self.s/2)
# class D(A):
#     def product(self):
#         print("product is ",self.x*self.y)

class A:
    def readEmployeeDetails(self):
        self.name=input("Enter Employee name :")
        self.age=input("Enter employee age :")
class B:
    def readSalaryDetails(self):
        self.des=input("Enter Employee designation :")
        self.sal=input("Enter employee Salary :")
class C(A,B):
    def Employeedetails(self):
        print("Name of Employee is",self.name)
        print("Age of Employee is",self.age)
        print("Designation of Employee is ",self.des)
        print("Salary of Employee is ",self.sal)

obj=C()
obj.readEmployeeDetails()
obj.readSalaryDetails()
obj.Employeedetails()


# polymorphism - One_In-Many Forms
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
#

