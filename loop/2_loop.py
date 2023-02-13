# for i in [10,20,30]:
#     print(i)
#
# for i in 'python':
#     print(i)
#
# for i in range(1,10):
#     print(i)

# #print fibonacci series with for loop(with rng method)
# #0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
# n=int(input("Enter the number of elements :"))
# a,b=0,1
# print("Fibonacci series")
# print(a)
# print(b)
# for i in range(3,n+1):
#     c = a + b
#     print(c)
#     a,b=b,c


# #program to check whether given number is prime or not
#
# num=int(input("Enter your number :"))
# f = 0
# if num==1:
#     print('not defined')
# else:
#     for i in range(1,num+1):
#         if num%i==0:
#             f = f + 1
#     if f==2:
#         print('prime')
#     else:
#         print('not prime')

# for i in 'python':        #Can use else in for loop also
#     print(i)
# else:
#     print('completed')

# # Break statement is used to exit from the loop even if the condition is true
#
# l=[10,20,30,50,100,60,70,80]
# for i in l:
#     print(i)
#     if i == 100:
#         break


#continew statement is used to stop current iteration

l=[10,20,30,50,100,60,70,80]
for i in l:
    if i == 100:
        continue
    print(i)