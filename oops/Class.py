#oops
# class - object

# class Emp:
#     def display(self):
#         print('simple function')
#
# obj=Emp()
# obj.display()

# class Employee:
#     id = 10
#     name = "John"
#     def display(self):
#         print("ID: %d \nName: %s" % (self.id, self.name))
# emp = Employee()
# emp.display()
# print(emp.name)
# print(emp.id)

# class Emp:
#     name1="sree"
#     def display(self):
#         print('simple function')
#     def dis():
#         print("without self parameter ")
#     def sum(self,a,b):
#         print("sum is ",a+b)
#     def product(self,a,b):
#         print("Product is",a*b)
# obj=Emp()
# obj.display()
# print(obj.name1)
# obj.sum(40,50)
# obj.product(40,50)
# ob=Emp
# ob.dis()

# #Self parameter
# class Calc:
#     def item(self,a,b):
#         self.x=a
#         self.y=b
#     def sum(self):
#         print(self.x,"+",self.y,"=",self.x+self.y)
#     def product(self):
#         print(self.x,"-",self.y,"=",self.x*self.y)
#     def division(se):
#         print(se.x,"/",se.y,"=",se.x/se.y)
#     def subtraction(div):
#         print(div.x,"-",div.y,"=",div.x-div.y)
#
# obj=Calc()
# a = int(input("Enter first number"))
# b = int(input("enter second number"))
# obj.item(a,b)
# obj.sum()
# obj.product()
# obj.division()
# obj.subtraction()


# To find factorial of a number using class with function and return value

class Fact:
    def fac(self,n):
        f=1
        for i in range(1,n+1):
            f = f * i
        return f
obj=Fact()
n = int(input("Enter number :"))
f=obj.fac(n)
print("factorial is ",f)







