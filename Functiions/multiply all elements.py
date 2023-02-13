#Multiply all the numbers in a list using function
def mul():
    m = 1
    lst1=[5,5,2]
    for ele in lst1:
        m=m*ele
        ele+=1
    return m
print(mul())



