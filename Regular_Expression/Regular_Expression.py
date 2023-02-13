# Regular Expression -sequence of characters used to form a search pattern
# It is used to check if a string contains the specified search pattern
# Python has a built-in package called "re" which can be used to work with regular expression

# # findall() - It returns a list containing all matches
#
# import re
# str1="Life is full of surprises and miracles !"
# s=re.findall("Life",str1)
# print(s)
#
# s1=re.findall("surprises",str1)
# print(s1)
#
# s2=re.findall("fullll",str1)
# print(s2)

# import re
# d="cat mat rat pat sat"
# a=re.findall("[m]",d)
# print(a)
#
# a1=re.findall("[m]at",d)
# print(a1)
#
# a2=re.findall("[pa]",d)
# print(a2)

# import re
# d="cat mat rat pat sat"
# b=re.findall("[^c]",d)
# print(b)
# b1=re.findall("[^at]",d)
# print(b1)

# import re
# d="cat mat rat pat sat 99988 999"
# a=re.findall("\d{2}",d)
# print(a)
# b=re.findall("\d{3}",d)
# print(b)
# c=re.findall("\d{4}",d)
# print(c)
#
# d=re.findall("\d{1,4}",d)
# # print(d)
#
# import re
# d="cat mat rat pat sat 99988 999 8888 77777 93847 6543 654277"
# a=re.findall(r"\b\d{4}\b",d)
# print(a)

#search()- It returns a match object if there is a mach anywhere in the string
import re

str1="class will start at 10am"
s=re.search('\s',str1)
print(s)                            #This will print the location of white space (Both starting and ending)
print(s.start())                    #This will print starting location of white space

s1=re.search('\d',str1)
print(s1.start())

s2=re.search("python",str1)
print(s2)

