#function
#OOPs-Programs are based on class and object
#class - class is the way to bind functions and its related datas.
#Object - Instance of class or runtime entity of a class

#Function -Repeated group of statments / We can create a function for particular task
        # Mainly two parts --
        # Function definition and function calling
#return value - We can pass only on value from function definition to function calling is called return value
#function parameters -- we can pass more than one values from function calling to function definitions
#   Are called function parameters


# def sum():                          #Function definition
#     a,b=10,20                       #Function definition
#     s=a+b                           #Function definition
#     return s                        #Function definition
# print("Sum is ",sum())              #Function calling

# def sum(x,y):                       #x,y are parameters
#     s=x+y
#     return s
# print("Sum is ",sum(100,200))       #100,200 are parameters
# print("Sum is",sum(500,100))        #500,100 are parameters

# #Write a program to find factorial of a number using function with return type and function parameters
# num=int(input("Enter the number :"))
# def fact():
#     fac = 1
#     for i in range(1,num+1):
#         fac = fac * i
#     return fac
# print("Factorial of",num,"is",fact())

#Function parameters
#Simple,Arbitrary,Keyword,Default parameter value,List

# #Arbritrary
#
# def color(*args):
#     print(args[0])
#     for i in args:
#         print(i)
# color('red','white','black')
#
# def vehicle(*car):
#     print(car[0])
#     for i in car:
#         print(i)
# vehicle("benz","bmw","audi")

# def vehicle(x,*car):
#     print(car[0])
#     for i in car:
#         print(i)
# vehicle("benz","bmw","audi")

# #keyword arguments
#
# def stud(str1,str2,str3):
#     print('first ',str1)
#     print('second',str2)
#     print('third',str3)
# stud(str3='anu',str1='sree',str2='jith')

# def student(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
# student(str3='anu',str1='sree',str2='jith')

# def student(x,*args,**kwargs):
#     print("Simple argument :",x)
#     for j in args:
#         print("Arbritrary argument:",j)
#     for i,j in kwargs.items():
#         print("Keyword argument",i,j)
# student('jeffin','leo',str3='anu',str1='sree',str2='jith')


# #default parameter
#
# def display(country="india"):
#     print("Im from ",country)
# display()
# display("america")

# #list parameter
#
# def dis(ls):
#     for i in ls:
#         print(i)
# dis([10,20,30])

#Create a function to form a list taking inputes from user
#create an inner function to search an element in the string
#Create an inner function to remove an element from the string
#create an inner function to replace an element in the string
ls=[]
def create():
    num=int(input("Enter number of elements in the list :"))
    for i in range(num):
        ele=int(input("Enter your elements :"))
        ls.append(ele)
    print(ls)
def search():
    ele =int(input("enter the item to be searched:"))
    if ele in ls:
        print("Item Found")
    else:
        print("Item Not Found")
def remove():
    ele=int(input("Enter the element which needs to remove :"))
    if ele in ls:
        ls.remove(ele)
        print(ls)
    else:
        print(ele,"Is not in the list")
def replace():
    rep1 = int(input("Which item wants to be replaced :"))
    rep2 = int(input("Please enter the new element :"))
    for i in range(len(ls)):
        if ls[i]==rep1:
            ls[i]=rep2
            print(ls)

while True:
    print("1:Create\n2:Search\n3:Remove\n4:Replace")
    opt=int(input("Enter yor choice :"))
    if opt==1:
        create()
    elif opt==2:
        search()
    elif opt==3:
        remove()
    elif opt==4:
        replace()
    else:
        break






