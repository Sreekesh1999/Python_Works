#genarate a python function to print all even numbers between 4 and 30

def even():
    lst1 = []
    for i in range(4,30):
        if i % 2 == 0:
            lst1.append(i)
    return lst1
print(even())
