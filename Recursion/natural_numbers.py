# Sum of natural numbers using recursion
def num(n):
    if (n>0):
        result = n + num(n-1)
        print(result)
    else:
        result = 0
    return result
print(num(10))