# write a python function to create and print a list where the values are squere of numbers
# between 1 and 30 (both included )
def squares():
    lst1 = []
    for i in range(1,31):
        i = i**2
        lst1.append(i)
    return lst1
print(squares())