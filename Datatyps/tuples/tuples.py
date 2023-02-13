tpl1=(1,2,3,4,5,6,7,8,9,10,"sree")  #creating tuple #multiple datatyps are possible
# print(tpl1)
# print(type(tpl1))
#
# tpl2=[1,2,3,4,5,6,7,8,9,10,"sree"]  #converting list to tuple
# print(tuple(tpl2))
#
# print(len(tpl2))  # finding length of tuple
#
# print(tpl1[5])   #accesing elements using index values
# print(tpl1[-1])
#
# print(tpl1[0:3])   #slicing
#
# print(tpl1[:-5])
# print(tpl1[-4:-1])
#
# print(tpl1[::-1])  #reverse of a tuple
#
# y = list(tpl1)  #updating values to tuple
# y[0]="sreekesh"
# tpl1 = tuple(y)
# print(tpl1)
#
# lst2=list(tpl1)  #append values to tuple
# lst2.append("sreejith")
# print(lst2)
# tpl1=tuple(lst2)
# print(tpl1)
#
# tpl3=(100,123,234,56,456,345,76,98)  #concatinating 2 tupls
# tpl4=tpl1+tpl3
# print(tpl4)
#
# x = list(tpl4)   #remove elements from tuple
# x.remove("sreejith")
# x.remove(100)
# tpl4 = tuple(x)
# print(tpl4)
#
# # del tpl4  #deleting tuple #will get tpl4 is not defined error
# # print(tpl4)
#
# fruits = ("apple", "banana", "cherry")  #unpacking tuple
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)
#
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry") #unpacking tuple
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# thistuple = ("apple", "banana", "cherry") #printing tuple using loop #for
# for x in thistuple:
#   print(x)

# for i in range(len(thistuple)):
#     print(thistuple[i])

# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1

# tpl5 = ("sreekesh",[1,2,3,4,5],("Audi","bmw","benz"))  #nested tuple
# print(tpl5)             #accessing values in nested list
# print(tpl5[0])
# print(tpl5[1])
# print(tpl5[2])
# print(tpl5[0][0])
# print(tpl5[1][0])
# print(tpl5[2][0])
# print(tpl5[2][1])
#
# tpl5[1][2] = 100   #changing elements of a list incide tuple
# print(tpl5)

fruits = ("apple", "banana", "cherry","mango","berry",)  #to repeate same tuple
# mytuple = fruits * 2
# print(mytuple)
#
# print("apple" in fruits)
# print("apple" not in fruits)


# print(all(fruits))     # all method - Returns false if list contain False or 0. else return true
# fruits1 = ("apple", "banana", "cherry","mango","berry",False)
# print(all(fruits1))
# fruits2 = ("apple", "banana", "cherry","mango","berry",0)
# print(all(fruits2))

# str1 =(1,2,3,4,5,6,7,0,9,66)
# print(len(str1))
# print(all(str1))
# print(max(str1))
# print(min(str1))
# print(sorted(str1))
# print(sum(str1))


# x = ('python','java','express')   #enumarate
# y = enumerate(x)
# print(tuple(y))
#
# names = ("Sree","Jeffin","Leo")
# ages = (23,24,25)
# job = ("Teacher","IT","Actor")
#
# for i, (names,ages,job) in enumerate(zip(names,ages,job)):
#     print(i,names,ages,job)

# letters = [('a','A'),('b','B')]
# for i,letters in enumerate(letters):
#     print("Letter %d is %s/%s" % (i,letters[0],letters[1]))

# l = ["sat","cat","bat","mat"]  #map
# test = tuple(map(tuple,l))
# print(test)



