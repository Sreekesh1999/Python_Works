# #Lambda functions - lambda function is a small anonymous function.It can take any number of
# # arguments but can only have one expression
#
# def sum(a,b):
#     return a+b
# print(sum(10,20))
#
# #Syntax;lambda arguments:expression
# add=lambda a,b:a+b
# print(add(2,3))
#
# sub=lambda a,b:a-b
# print(sub(10,5))

# largest=lambda a,b:a if(a>b) else b
# print(largest(100,200))

# #filter,map,reduce
# l=[10,20,76,31,30,40,50,60]
# lst=list(filter(lambda x:x%2==0,l))
# print(lst)
#
# lst1=list(filter(lambda x:x%2!=0,l))
# print(lst1)
#
#
# #map
# lst1=list(map(lambda x:x%2!=0,l))
# print(lst1)
#
# lst=list(map(lambda x:x%2==0,l))
# print(lst)
#
# lst=list(map(lambda x:x*2,l))
# print(lst)
#
# lst=list(map(lambda x:x>2,l))
# print(lst)
#
# lst=list(map(lambda x:x+2,l))
# print(lst)

#reduce

from functools import reduce
l1=[10,20,76,31,30,40,50,60]
product=reduce(lambda x,y:x*y,l1)
print(product)

from functools import reduce
l1=[10,20,76,31,30,40,50,60]
sum=reduce(lambda x,y:x+y,l1)
print(sum)

#What are the difference between lambda function and user defined function


