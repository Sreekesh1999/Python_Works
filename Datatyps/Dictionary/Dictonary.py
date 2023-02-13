# #Create a dictionary taking input from user
dic={}
number=int(input("Enter the number of elements :"))
for i in range(number):
    key=input("Enter the key :")
    value=input("Enter the value :")
    dic.update({key:value})
print(dic)

# dic = {"Name":"Sreekesh","Age":"23","cours":"python","job":"Tcs"}
# for i in dic.keys():
#     print(i)
# for i in dic.values():
#     print(i)
# for i in dic.items():
#     print(i)
# for i,j in dic.items():
#     print(i,j)
#
# x=dic.get('Name')   #to get value using key
# print(x)
