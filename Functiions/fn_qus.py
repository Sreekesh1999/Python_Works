#write a python program to find the max of 3 numbers

# def max(a, b, c):
# 	if (a >= b) and (a >= c):
# 		largest = a
# 	elif (b >= a) and (b >= c):
# 		largest = b
# 	else:
# 		largest = c
# 	return largest
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# c = int(input("Enter third number :"))
# print("Largest is ", max(a, b, c))

#write a python program to find sum of all numbers in a list
def sum():
	s = 0
	for i in lst1:
		s = s + i
		i += 1
	return s
lst1 = [1,2,34,5]
print(sum())

#write a python function to multiply all thr numbers in a list
def mul():
	s = 1
	for i in lst1:
		s = s * i
		i += 1
	return s

lst1 = [1,2,3,4,5]
print(mul())