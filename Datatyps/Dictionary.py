dict = {"Name":"Sreekesh","Age":"23","cours":"python","job":"Tcs"}   # creating dictonary
# print(dict)  #print dict
# print(type(dict))
# print(dict["Name"])    #accessing elements
# x = dict.get("cours")  #accessing elements
# print(x)
# print(dict.keys())   #accessing keys
print(dict.values())  #accessing values
print(dict.items())   #accessing both key and value as tuples

dict["Age"] = 30   #changing value of dict
print(dict)
dict["cours"] = "java"
print(dict)
#
# # dict.update({"Name":})
# # print(dict)
# dict["place":"Malappuram"]
# print(dict)

dict.update({"color":"red"})  #adding elements
print(dict)

dict.pop("color")  #removing elements
print(dict)

dict.popitem()  #Removing last item
print()

# del dict     #Delete the dictionary
# print(dict)

# dict.clear()   #clear the dictionary
# print(dict)

# for i in dict:    #Accesing dict elements using loop
#     print(i)
#
# for i in dict.keys():
#     print(i)
#
# for i in dict.values():
#     print(i)
#
# for i in dict.items():
#     print(i)

print(dict.copy())  #copy dict