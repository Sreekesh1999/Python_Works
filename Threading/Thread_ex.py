# Threading
# Thread means part of a program or lightweight process
# Two types - single threading and multi threading #

# from time import sleep
# def task():
#     #block for a moment
#     sleep(2)
#     #Display a message
#     print("This is from another thread")
# # task()
#
# from threading import Thread
# #create a thread
# thread=Thread(target=task)
# #Next, we can create an instance of the threading. Thread class and specify
# # our function name as the "target" argument in the constructor.
# # run the thread#
# thread.start()
#
# from time import sleep
# from threading import Thread
#
# def task(sleep_time,message):
#     #block for a moment
#     sleep(sleep_time)
#     #display a message
#     print(message)
#
# # Create a thread
# thread=Thread(target=task,args=(5,"New message from another thread"))
# # Run the thread
# thread.start()
# # Wait for the thread to finish
# print("Waiting for the thread...")
# thread.join()

import time
import threading

def cal_squre(num):
    print("Calculate the square root of given number ")
    for n in num:
        time.sleep(0.3) # at each iteration it waits for 0.3 seconds
        print("square is ", n * n)
def cal_cube(num):
    print("Calculate the cube of given number ")
    for n in num:
        time.sleep(0.3) # at each iteration it waits for 0.3 seconds
        print("cube is ", n * n * n)
arr = [4,5,6,7,2]

t1=time.time()
# cal_cube(arr)
# cal_squre(arr)
th1=threading.Thread(target=cal_squre,args=(arr,))
th2=threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("Total time taken by thread is :", time.time()-t1) #print total time


