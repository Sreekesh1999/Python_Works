#Exception notes will be ther in thre whatspp group#

try:
    n1=int(input("Enter first number :"))
    n2=int(input("Enter second number :"))
    res=n1/n2
    print("Output is ",res)
except Exception as ex:
    print(ex)
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#     print(er)