# # # 1. add list of elements to a set
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# set10 = {10,20,30,40}
#
# set10.update(lst1)
# print(set10)


# # #2.Check if two sets have any elements in common. if yes ,display the common elements
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
# # print("Common elements are ",set1 & set2)
#
# #3. Remove items from set1 that are not common to both set1 and set 2
#
set3 = set(set1 - set2)
print(set3)
print(set1 - set3)
#
# #4. Get only unique items from two sets
# set4 = set(set2 - set1)
# print(set3)
# print(set4)
# set5 = set3 | set4
# print(set5)




