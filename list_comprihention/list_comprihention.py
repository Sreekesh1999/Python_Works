# fruits = ["apple","banana","cherry","orange"]
# print(fruits)
#
# nwlist = [x for x in fruits if "a" in x]
# print(nwlist)
#
# nwlist1 = [x for x in fruits if x!="banana"]
# print(nwlist1)
#
# print([x for x in "Hello world"])
#
# print([x for x in range(10)])
# print([x for x in range(10) if x<5 ])

# #Remove all odd numbers from the below list
# numbers = [3,5,45,97,32,22,10,19,39,43]
#
# nwlst = [x for x in numbers if x%2==0]
# print(nwlst)

# # create a list containing 1 to 100
# lst1 = [x for x in range(1,101)]
# print([x for x in lst1 if x%2==0])
# print([x for x in lst1 if x%2!=0])

#sum of n natural numbers upto 10
a = int(input("Enter starting range : "))
b = int(input("Enter ending range: "))
num = [x for x in range(a,b)]
print(num)
print("Sum of above is: ",sum(num))
