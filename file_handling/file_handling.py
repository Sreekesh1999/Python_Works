#file handling
#file handling is an important part of any web application.Python has several functions for creating,
#reading,updating and deleting files.
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename and mode
# There are four different methods(modes) for opening a file:

# "r"-Read - Default value.Opens a file for reading ,error if the file does not exist #
# "a"- Append -Opens a file for appending,creates the file if it does not exist
# "W"- Write -Opens a file for writing ,Creates the file if it does not exist
# "X"- Create -Creates the specified file,returns an error if the file exists
# #

#Read
# f=open("test","r")
# print(f.read())
# print(f.read(8))
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for i in f:
#     print(i)
# f.close()


# o=open("filehandling","r")
# print(o.read())

#Append
#Append the content to the end of the file #

# f=open("test","a")
# # f.write(".Python is a oop")
# # f.close()
# f=open("test","r")
# print(f.read())


# f=open("test","r")
# for i in f:
#     print(i)
# f.close()

#Write
# # #
# f=open("test","w")
# f.write("Im replacing all the stuffs")
# f.close()

# f=open("test","r")
# print(f.read())
# f.close()

# Seek()
# Seek method sets the current file position in a file stream
# It also returns the new position
# Syntax : file.seek(offset)
# #
# f=open("test","r")
# f.seek(6)
# print(f.readline())
# f.close()

# tell()
# It returns the current position of the file
# Syntax: fileobject.tell()
# #
# f=open("test","r")
# f.readline()
# pos=f.tell()
# f.close()
# print('position is',pos)

#Write a program to read a file line by line and store it into a list
# #
# def file_read(fna):
#     with open(fna) as f:
#         output_list=f.readlines()
#         print(output_list)
# file_read("test")

#copy file
# from shutil import copyfile
# copyfile("test","test1")

# Write a program to find number of words and convert it into dict
# str="cat rat mat cat pat rat cat sat cat sat"
# print(str)
# lst=str.split()
# print(lst)
# d={}
# for i in lst:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

f=open("test","r")
dic={}
for i in f:
    var=i.split(" ")
    for j in var:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
print(dic)
