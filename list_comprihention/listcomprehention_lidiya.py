#List comprehension - list comprehension provides an easy way to apply operations on a list
#it creates a new list in which each element is the result of applying a given operation in a list

# #Remove all odd numbers from the below list
# numbers = [3,5,45,97,32,22,10,19,39,43]
#
# nwlst = [x for x in numbers if x%2==0]
# print(nwlst)

# #syntax:list=[expression for item in list if condition]
#
# l=[x+3 for x in [1,2,3,4,5]]
# print(l)
#
# l1=[x*2 for x in [1,2,3,4,5,6,7,8,9,10]]
# print(str(l1))


# l2=[]
# n=int(input("Enter your limit :"))
# for i in range(1,n+1):
#     l2.append(i)
# print(l2)
# l3=[x for x in l2 if x%2==0]
# print(l3)

# l=[i for i in range(25) if i%2==0]
# print(l)
#
#
# vow=[i for i in "sreekesh" if i in ['a','e','i','o','u']]
# print(vow)

# str1="how are you"
# l=[]
# words=str1.split()
# print(words)
# for i in words:
#     x=i[0]
#     l.append(x)
# # print(l)
#
# str1=input("Enter your string :")
# words=str1.split()
# first_letter=[i[0] for i in words]
# print(first_letter)

# ele=input("Enter your letter :")
colors=['red','white','green','pink']
# col=[i for i in colors if ele in i]
# print(col)
#
# col1=[i for i in colors if i!="green"]
# print(col1)

newlist=[i.upper() for i in colors]
print(newlist)

newlist=['hello' for i in colors]
print(newlist)

newlist=[i if i!='pink' else 'blue' for i in colors]
print(newlist)

words="hai how are you"
num=[]

