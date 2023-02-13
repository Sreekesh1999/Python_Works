# Generate a Python list of all the even numbers between 4 to 30
# Expected o/p:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
lst1=[]
def even():
    for i in range(4,30):
        if i%2==0:
            lst1.append(i)
            i+=1
    return lst1
print(even())

