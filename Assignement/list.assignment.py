# def list1():
#     lst = []
#     n = int(input("Enter number of elements : "))
#     for i in range(0, n):
#         ele = int(input())
#         lst.append(ele)  # adding the element
#     print(lst)
# list1()

# #1.	Sum of all the items in a list
# mylist = [1,2,3,4,5]
# print(mylist[0]+mylist[1]+mylist[2]+mylist[3]+mylist[4])

#2.	Write a Python program to get the largest number from a list.
# mylist = [1,2,-8,0]
# num1=(mylist[0])
# num2=(mylist[1])
# num3=(mylist[2])
# num4=(mylist[3])
#
# if num1>num2 and num1>num3 and num1>num4:
#     print(num1,"is greater than",num2,num3,"and",num4)
# elif num2>num1 and num2>num3 and num2>num4:
#     print(num2,"is greater than",num1,num3,"and",num4)
# elif num3>num1 and num3>num2 and num3>num4:
#     print(num3,"is greater than",num2,num1,"and",num4)
# else:
#     print(num4,"is greater than",num1,num2,"and",num3)

# #3.	Write a Python program to convert a list of characters into a string
# mylist = ["p","y","t","h","o","n"]
# print(mylist)
# mylist1 = (mylist[0]+mylist[1]+mylist[2]+mylist[3]+mylist[4]+mylist[5])
# print(type(mylist1))

#Write a Python program to multiply all the items in a list.

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
        ele = int(input())
        lst.append(ele)  # adding the element
print("Your list :",lst)

mul = 1
for x in (lst):
        mul = mul * x
print("Multiplied value of numbers in the given list is :",mul)












