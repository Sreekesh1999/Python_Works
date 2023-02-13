#number
num = 5
print(num)

#string #immutable
name = "sree"
age = '23'
print(type(name))
print(type(age))

#string indexing
str1 = "hello world"
print(str1)
print(str1[3]) #forward indexing
print(str1[4])
print(str1[-1])  # Negative indexing # printing from reverse
print(str1[-2])

#string slicing
print(str1[0:5])  # to access hello only from the string
print(str1[:-1])
print(str1[::-1]) # to complete reversal of a string
print(str1[::-2]) # to remove alternative items from reversal
print(str1[::-3])
print(str1[-6:])
print(str1[-1:-6:-1])

#methods
print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.swapcase())

str2 = "Hellow world"
print(str2.isupper())   #returns true if all characters are uppercase
print(str2.islower())   #returns true if all characters are lowercase
print(str2.isalpha())   #returns true if all items are characters

#List
list1 = [1,4,34,345,65]
print(list1)
print(type(list1))

#dict
dict = {"name" : 12}
print(dict)
print(type(dict))

#set
set = {1,23,4,5,6}
print(set)
print(type(set))

#tuple
a = "sree","kesh","kp"
print(a)
print(type(a))

