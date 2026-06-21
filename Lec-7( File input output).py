<<<<<<< HEAD
#------------------------------------------- Opening a file with Python to read only .-------------------------------------------------------------

"""f=open("name(with type) or complete path of the file"," mode in which we want to open the file")

data=f.read()                       # This is the syntax
print(data)                         # prints what's inside the file for us to read
f.close()"""                        # closes the file( will not open until we run it), signs of a good programmer

#(A): The file is in the same folder as of this python file.

"""g=open("same_folder.txt","r")        # when the file is in same folder as of this python file we just need to write the name (along with type->.txt,.docx,etc) to open it

x=g.read()
print(x)
g.close()"""

#(B): The file is in the different(or even in a folder within the current folder) folder as of this python file.

"""p=open("D:\\PYTHON_CODES\\Just_for_lec_7/other_folder.txt","r")            # write the complete "file" path(not folder path)

data=p.read()                     # to open a file which is not in the same folder( or inside a folder within this folder) we have to write its complete path
print(data)
p.close()"""

#(C): Text mode (default mode):

""""a=open("same_folder.txt","rt")                        # r is the reading mode and t is the text mode. both are default modes so if havent wrote anything it would still do the same work

b=a.read()              
print(b)
a.close()"""

#(D): Reading characters :

"""q=open("same_folder.txt","rt")

n=int(input("Enter number of characters: "))

file=q.read(n)
print(file) """                                               # it will only read n number of characters.(spaces are also counted as characters)

#(E): Reading line by line.

"""o=open("same_folder.txt",)

line1=o.readline()                                     # prints only the first line and a blank second line due to reading "\n"  at the end of first line 
print(line1)    

line2=o.readline()
print(line2)"""

#(F): Printing text before readline

"""o=open("same_folder.txt",)

doc=o.read()
print(doc)                                           # if the entire file is printed or read before readline, readline will not be executed

line1=o.readline()                                   # to do this first close the file and then reopen this
print(line1)    

line2=o.readline()
print(line2)

o.close()"""

# ------------------------------------------Writing a file.--------------------------------------

#(A): 'w' method(truncating)

"""j=open("demo.txt","w")
trunc=j.write("No only serious talks.\nNo non serious talks")              # This will erase everything written in demo.txt and only write this string in it
j.close()"""
# print(trunc)                                      # it will only print the numer of characters in "No only serious talks, It will not print the string itself"

#(B): 'a' method(append)

"""h=open("sample.txt","a")

appe=h.write("\nAfter that i will try to build some projects,\nI will probably give ZCO")           # This will add these two lines at the end of the existing text in sample.txt

h.close()"""
# print(appe)                                   # This will also print no. of characters stored in appe

#(C): Opening a non existing file:

# If we open a non existing file in python in "w" or "a" mode, python automatically creates that file for us in the same folder( created file do not have any pre-existing text in it)

"""v=open("Non_existing_1.txt","w")
v.close()

w=open("Non_existing_2.txt","a")
w.close()"""

# All those a+,r+ and w+ modes are there but they are too tedious

# "with" Syntax

"""with open("sample.txt","r") as f:
    data=f.read()
print(data)"""

"""with open("sample.txt","w") as f:
    f.write("Or maybe this will all remain unachived ")"""

# Deleting a file:

"""import os
os.remove("Demo.txt")"""

#--------------------QUESTION PRACTICE---------------------#

#(Q1) : Create a new file "practice.txt" using python. Add the following data in it:
#         Hi everyone
#         we are learning File I/O
#         using Java
#         I like programming in Java

"""f=open("practice.txt","w")                                                                           # we could have also used 'a'
file1=f.write("Hi everyone \nwe are learning File I/O \nusing Java \nI like programming in Java")
f.close()  """                                                                                          # without closing we can't do next works

#(Q2): WAF that replaces all occurrences of "java" with "python"

"""with open("practice.txt","r") as b:
    data=b.read()
    print(data)
print(type(data))
change=data.replace("Java","Python")                          # this only changes the words and prints them
print(change)

with open("practice.txt","w") as g:                            # this rewrite the data in the original file
    g.write(change)"""

#(Q3): Search if the word "learning" exists in the file or not

"""word="learning"
with open("practice.txt","r") as j:      
    work=j.read()
    if (work.find(word)!= -1):          
        print("Word Found")
    else:
        print("Not Found")"""

# it can also be done by a function

# def word_finder():
#     word="learning"
#     with open("practice.txt","r") as j:      
#         work=j.read()
#         if (word in work):                               # better syntax
#             print("Word Found")                        
#         else:
#             print("Not Found")
                                                           
# word_finder()
                                  
#(Q4) : WAF to find in which line of the file does the word "learning" occurs first. Print -1 if word is not found

"""def line_finder():
    word="learning"
    data = True
    line_no=1
    with open("practice.txt","r") as j:
        while data:
            data=j.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    print(-1)
    return -1
    
   

line_finder()"""

#(Q5): From a file containing numbers seperated by comma, print the count of even numbers.



=======
#------------------------------------------- Opening a file with Python to read only .-------------------------------------------------------------

"""f=open("name(with type) or complete path of the file"," mode in which we want to open the file")

data=f.read()                       # This is the syntax
print(data)                         # prints what's inside the file for us to read
f.close()"""                        # closes the file( will not open until we run it), signs of a good programmer

#(A): The file is in the same folder as of this python file.

"""g=open("same_folder.txt","r")        # when the file is in same folder as of this python file we just need to write the name (along with type->.txt,.docx,etc) to open it

x=g.read()
print(x)
g.close()"""

#(B): The file is in the different(or even in a folder within the current folder) folder as of this python file.

"""p=open("D:\\PYTHON_CODES\\Just_for_lec_7/other_folder.txt","r")            # write the complete "file" path(not folder path)

data=p.read()                     # to open a file which is not in the same folder( or inside a folder within this folder) we have to write its complete path
print(data)
p.close()"""

#(C): Text mode (default mode):

""""a=open("same_folder.txt","rt")                        # r is the reading mode and t is the text mode. both are default modes so if havent wrote anything it would still do the same work

b=a.read()              
print(b)
a.close()"""

#(D): Reading characters :

"""q=open("same_folder.txt","rt")

n=int(input("Enter number of characters: "))

file=q.read(n)
print(file) """                                               # it will only read n number of characters.(spaces are also counted as characters)

#(E): Reading line by line.

"""o=open("same_folder.txt",)

line1=o.readline()                                     # prints only the first line and a blank second line due to reading "\n"  at the end of first line 
print(line1)    

line2=o.readline()
print(line2)"""

#(F): Printing text before readline

"""o=open("same_folder.txt",)

doc=o.read()
print(doc)                                           # if the entire file is printed or read before readline, readline will not be executed

line1=o.readline()                                   # to do this first close the file and then reopen this
print(line1)    

line2=o.readline()
print(line2)

o.close()"""

# ------------------------------------------Writing a file.--------------------------------------

#(A): 'w' method(truncating)

"""j=open("demo.txt","w")
trunc=j.write("No only serious talks.\nNo non serious talks")              # This will erase everything written in demo.txt and only write this string in it
j.close()"""
# print(trunc)                                      # it will only print the numer of characters in "No only serious talks, It will not print the string itself"

#(B): 'a' method(append)

"""h=open("sample.txt","a")

appe=h.write("\nAfter that i will try to build some projects,\nI will probably give ZCO")           # This will add these two lines at the end of the existing text in sample.txt

h.close()"""
# print(appe)                                   # This will also print no. of characters stored in appe

#(C): Opening a non existing file:

# If we open a non existing file in python in "w" or "a" mode, python automatically creates that file for us in the same folder( created file do not have any pre-existing text in it)

"""v=open("Non_existing_1.txt","w")
v.close()

w=open("Non_existing_2.txt","a")
w.close()"""

# All those a+,r+ and w+ modes are there but they are too tedious

# "with" Syntax

"""with open("sample.txt","r") as f:
    data=f.read()
print(data)"""

"""with open("sample.txt","w") as f:
    f.write("Or maybe this will all remain unachived ")"""

# Deleting a file:

"""import os
os.remove("Demo.txt")"""

#--------------------QUESTION PRACTICE---------------------#

#(Q1) : Create a new file "practice.txt" using python. Add the following data in it:
#         Hi everyone
#         we are learning File I/O
#         using Java
#         I like programming in Java

"""f=open("practice.txt","w")                                                                           # we could have also used 'a'
file1=f.write("Hi everyone \nwe are learning File I/O \nusing Java \nI like programming in Java")
f.close()  """                                                                                          # without closing we can't do next works

#(Q2): WAF that replaces all occurrences of "java" with "python"

"""with open("practice.txt","r") as b:
    data=b.read()
    print(data)
print(type(data))
change=data.replace("Java","Python")                          # this only changes the words and prints them
print(change)

with open("practice.txt","w") as g:                            # this rewrite the data in the original file
    g.write(change)"""

#(Q3): Search if the word "learning" exists in the file or not

"""word="learning"
with open("practice.txt","r") as j:      
    work=j.read()
    if (work.find(word)!= -1):          
        print("Word Found")
    else:
        print("Not Found")"""

# it can also be done by a function

# def word_finder():
#     word="learning"
#     with open("practice.txt","r") as j:      
#         work=j.read()
#         if (word in work):                               # better syntax
#             print("Word Found")                        
#         else:
#             print("Not Found")
                                                           
# word_finder()
                                  
#(Q4) : WAF to find in which line of the file does the word "learning" occurs first. Print -1 if word is not found

"""def line_finder():
    word="learning"
    data = True
    line_no=1
    with open("practice.txt","r") as j:
        while data:
            data=j.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    print(-1)
    return -1
    
   

line_finder()"""

#(Q5): From a file containing numbers seperated by comma, print the count of even numbers.



>>>>>>> 2a93e30f2786d5dd7afc8fccd2d3532927786842
