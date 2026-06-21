<<<<<<< HEAD
# Introduction and needs of loops
# Taks : Print "Hello" 5 times
# method-1
"""print("Hello")
print("Hello")                    # write print("Hello") one and copy it 5 times. It becomes ineffective when said to print 100 or 1000 times
print("Hello")
print("Hello")
print("Hello")

# method-2                        # the process of each loop is called iteration
count=1                           # we could have used any variable in place of count, its defined to break the loop from running infinitely
while(count<=5):                  # count is a variable called iterator. Its value starts from 1 and till its value remains <= 5 , the contion remains true and the whole loop keeps working
    print("Hello")                # till the while condition (count<=5) is true "Hello" keeps printing as "while" is a loop function
    count+=1                      # count increases at a rate of +1 every time he function is exectuted. so before count<=5, "Hello" will be printed 5 times
print(count)"""                   # count will be six as after 5 when count is 6 , hello will not get printed and hence counting will stop


# While Loops in python

#(A):

"""i=1                                     # i starts from 1
while(i<=10):                           # while i is within 10 , while condition is true
    print("Hey",i)                      # hey gets printed alond with value of i
    i+=1                                # as "Hey" gets printed for the first time , value of i also gets changed from 1 to 2 and so on...
print(i)"""                                # on i=11, the loop didn't print anything and hence counting of i stopped

#(B): Backward Counting

"""i=5                                         
while(i>=1):                              
    print("Good",i)
    i-=1
print("Loop ended")
print(i)"""

#(C): What happens if counting of variable starts before print

"""i=5                                         
while(i>=1):                      # print will start after the counting of the value and hence print will start from i+1
    i-=1                                   
    print("Good",i)
print("Loop ended")
print(i)"""

#(D): Printing numbers in loops

#Forward counting

"""i=1
while i<=7:
    print(i)                     # i during loop is ongoing
    i+=1
print(i)                         # i after loop ended 
print("Loop ended")"""

#Backward Counting

"""i=9
while i>=1:
    print(i)                     # i during loop is ongoing
    i-=1
print(i)                         # i after loop ended
print("Loop ended")"""

#(E): Infinite loop

"""i=1
while i>=0:                              # always true
    print(i)
    i+=1
print("Loop ended")"""                       # this will never gets executed as loop never ends.


# Question Practice :

#(Q1) : print numbers from 1 to 100:-

"""i=1
while i<=100:
    print(i)
    i+=1
print("Loop ended")
print("1 to 100 printed")"""

#(Q2) : print numbers  from 100 to 1

"""i=100
while i>=1:
    print(i)
    i-=1
print("loop ended")
print("printed 100 to 1")"""

#(Q3) : print multiplication table of a number n 

"""n=float(input("Enter your number: "))
i=1
while i<=10:
    print(n*i)
    i+=1
print("This is the multiplication table of",n,"upto 10 times")"""

#(Q4) : Print elements in the following list using a loop : [1,4,9,16,25,36,49,64,81,100]

"""squares=[]
i=1
while i<=10:
    squares.append(i**2)
    i+=1
print(squares)"""

# alt approach

"""nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i+=1"""
# Example:
"""heros=["Thor","Captain America","Ironman","Hulk","Hawkey"]
idx=0
while idx<=(len(heros)-1):
    print(heros[idx])
    idx+=1"""

#(Q5) : Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)
#(Done with help)

"""num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the value you want to search : "))
idx=0
while idx < len(num):
    if num[idx] == x:
        print("Value found at index", idx)
    else:
        print("Finding.....")
    idx+=1
print("End of list")"""


# Break and continue in loops

#(A): Break-> stops the loop immediately after a certain condition

#(1)
"""i=1
while i<=5:
    print(i)                 
    i+=1                     # here i+=1 is done prior of checking "if" condition, so by the time it prints 2, i becones 3 just after(due to i+=1 before if) , and the loop stops at i==3, hence it only prints 1 and 2 , inspite of i being 3
    if i==3:
        break
print("Loop ended at i=",i )
print(i)"""

#(2)
"""p=1
while p<=5:
    print(p)                
    if p==3:                 # here p+=1 is after the if condition so it first prints p , check value of p and then increases. So at p==3, it prints(p) , then (rather than increasing it to 4), checks the "if" condition and breaks after that 
        break
    p+=1
print("Loop ended at p=",p)
print(p)"""

#(3)
# Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)


"""num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the value you want to search : "))
idx=0
while idx < len(num):
    if (num[idx] == x):
        print("Value found at index", idx)
        break
    else:
        print("Value not found,Finding.....")
    idx+=1
print("End of list")"""

#(B): Continue-> skips in simple terms. terminates the ongoing loop on ground of some conditions and continues again 

#(1) : Skipping 3
"""i=0
while i<=5:
    if(i==3):
        i+=1
        continue                   # when i will be 0 it will print normally. When i==3 it will add 1 to it and again i==4 will be checked and cotinue to print. only when i==3 , it will satisfy the if condition and i will become 4 and continue the iteration, as no funtion after continue will be executed when i==3.
    print(i)    
    i+=1"""

#(2): Print only odd numbers from 1 to 100

"""i=0
while i<=100:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1"""

#(3): Print only even numbers from 1 to 100

"""i=0
while i<=100:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1"""


# For loops in python : There are used to travel through elements (check them or print) of a list , tuple or string .

#(A): Examples:

"""nums=[1,2,4,3,5,6,9]
for val in nums:              # val is a random variable representing each element individually in list
    print(val)  """              # it will print all the elements of nums list in the same order as of the list (val represent each element, we can further apply condition on "for " loop )

"""s="ApnaCollege"
for val in s:
    #print(s)                    # prints "ApnaCollege" as many times as there are characters in it which is 11          
    print(val)  """ 

#(B): Difference 

# using "for" loop
"""fruits=("mango","banana","apple","watemelon","litchi")
for a in fruits:
    print(a)
print("End of for loop")

# using "while" loop
vegitables=("onion","carrot","potato","brinjal","ladyfinger")
i=0
while i<len(vegitables):
    print(vegitables[i])
    i+=1
print("End of while loop")"""

#(3): Conditions on "for" loops

""""standard=[1,2,3,4,5,6,7,8,9,10,11,12]
for classes in standard:
    if(classes%2!=0):
        classes+=1         
        continue
    print(classes)
    classes+=1 """                # Prints only even classes

#(4): A nice problem:

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]"""

# Using while loop
"""nums=[2,7,11,15]
target = 9
i=0
while i<len(nums):
    j=i+1
    while j<len(nums):
        if(nums[i]+nums[j]==target):
            print([i,j])
            break
        j+=1
    i+=1"""

# Using for loop
"""nums=[2,7,11,15]
target = 9
for i in nums:
    j=i+1
    for j in nums:
        if(nums[i]+nums[j]==target):
            print([i,j])"""
            
# ====Question Practice==== #

#(Q1) : Print elements in the following list using a loop : [1,4,9,16,25,36,49,64,81,100]

"""squares=[1,4,9,16,25,36,49,64,81,100]
for nums in squares:
    print(nums)"""

#(Q2) : Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

"""squares=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number you want to search : "))
for nums in squares:
    if(nums==x):
        print("Number found at index->",squares.index(x))
        break
    else:
        print("Value not found. Finding..........")"""

# Alt approach:
"""nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number you want to search : "))
i=0
for el in nums:
    if(el==x):
        print("Number found at index->",i)
    i+=1"""

#================== Range()==================#

"""print(range(5))"""

# Different ways of using range

"""x=range(5)
for el in x:                            # USING STARTING VAL AND STEP IS COMPLETELY OPTIONAL. BY DEFAULT THEY ARE SET AS 0 AND 1 RESPECTIVELY
    print(el)

for p in range(5):                      # range(stoping val), ending value doesn't get printed
    print(p)

for m in range(0,6):                    # range(starting val, stopping val)
    print(m)

for n in range(0,10,2):                 # range(start,stop,step)
    print(n) """                          

# Printing of even number from 0 to 100

"""for el in range(0,100,2):
    print(el)   """                                # to include 100 also range(0,101,2)

#===================== Question Practice: =====================#

#(Q1): Using for and range() print numbers from 1 to 100

"""for nums in range(1,101):                 # if not assigned value it will take it as 1
    print(nums)"""

#(Q2): Print numbers from 100 to 1

"""for nums in range(100,0,-1):                            # withot the stepsize , dfault is (+1) hence it will not print anything starting from 100 and ending at 0
    print(nums)"""

#(Q3): Print the multiplication table of a number n upto 10 times:

"""n=float(input("Enter your number: "))

for i in range(1,11):
    print(n*i)
print("End of table")"""

# Pass Statement: If we wan to create a loop or a conditional statement and keep it blank we can't execute further function . Hence we use pass statement

"""i=0
while i<=77:                       # we can't leave loops blank and do next work


print("Next world")-------->error"""

"""for i in range(10):


print("Hola)-------------> error"""

"""a=10
b=9

if a==b:

print("Hello")----------->error"""

# With pass statement

"""i=0
while i<=77:
    pass                      

print("Next word")"""


#=================Questions===================#

#(Q1) : WAP to find the sum of first n numbers(using while):

"""print("=============Sum of first n natural number====================")
n=int(input("Enter number(n): "))
sum=0
i=0
while i<=n:
    sum+=i
    i+=1
    
print("Sum of first 'n' natural number is->",sum)"""

#(Q2) : WAP to find the factorial of first n natural number(using for):

"""print("============Factorial of first n natural number============")

n=int(input("Enter number(n): "))
factorial=1
for i in range(1,n+1,1):
    factorial*=i
=======
# Introduction and needs of loops
# Taks : Print "Hello" 5 times
# method-1
"""print("Hello")
print("Hello")                    # write print("Hello") one and copy it 5 times. It becomes ineffective when said to print 100 or 1000 times
print("Hello")
print("Hello")
print("Hello")

# method-2                        # the process of each loop is called iteration
count=1                           # we could have used any variable in place of count, its defined to break the loop from running infinitely
while(count<=5):                  # count is a variable called iterator. Its value starts from 1 and till its value remains <= 5 , the contion remains true and the whole loop keeps working
    print("Hello")                # till the while condition (count<=5) is true "Hello" keeps printing as "while" is a loop function
    count+=1                      # count increases at a rate of +1 every time he function is exectuted. so before count<=5, "Hello" will be printed 5 times
print(count)"""                   # count will be six as after 5 when count is 6 , hello will not get printed and hence counting will stop


# While Loops in python

#(A):

"""i=1                                     # i starts from 1
while(i<=10):                           # while i is within 10 , while condition is true
    print("Hey",i)                      # hey gets printed alond with value of i
    i+=1                                # as "Hey" gets printed for the first time , value of i also gets changed from 1 to 2 and so on...
print(i)"""                                # on i=11, the loop didn't print anything and hence counting of i stopped

#(B): Backward Counting

"""i=5                                         
while(i>=1):                              
    print("Good",i)
    i-=1
print("Loop ended")
print(i)"""

#(C): What happens if counting of variable starts before print

"""i=5                                         
while(i>=1):                      # print will start after the counting of the value and hence print will start from i+1
    i-=1                                   
    print("Good",i)
print("Loop ended")
print(i)"""

#(D): Printing numbers in loops

#Forward counting

"""i=1
while i<=7:
    print(i)                     # i during loop is ongoing
    i+=1
print(i)                         # i after loop ended 
print("Loop ended")"""

#Backward Counting

"""i=9
while i>=1:
    print(i)                     # i during loop is ongoing
    i-=1
print(i)                         # i after loop ended
print("Loop ended")"""

#(E): Infinite loop

"""i=1
while i>=0:                              # always true
    print(i)
    i+=1
print("Loop ended")"""                       # this will never gets executed as loop never ends.


# Question Practice :

#(Q1) : print numbers from 1 to 100:-

"""i=1
while i<=100:
    print(i)
    i+=1
print("Loop ended")
print("1 to 100 printed")"""

#(Q2) : print numbers  from 100 to 1

"""i=100
while i>=1:
    print(i)
    i-=1
print("loop ended")
print("printed 100 to 1")"""

#(Q3) : print multiplication table of a number n 

"""n=float(input("Enter your number: "))
i=1
while i<=10:
    print(n*i)
    i+=1
print("This is the multiplication table of",n,"upto 10 times")"""

#(Q4) : Print elements in the following list using a loop : [1,4,9,16,25,36,49,64,81,100]

"""squares=[]
i=1
while i<=10:
    squares.append(i**2)
    i+=1
print(squares)"""

# alt approach

"""nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i+=1"""
# Example:
"""heros=["Thor","Captain America","Ironman","Hulk","Hawkey"]
idx=0
while idx<=(len(heros)-1):
    print(heros[idx])
    idx+=1"""

#(Q5) : Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)
#(Done with help)

"""num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the value you want to search : "))
idx=0
while idx < len(num):
    if num[idx] == x:
        print("Value found at index", idx)
    else:
        print("Finding.....")
    idx+=1
print("End of list")"""


# Break and continue in loops

#(A): Break-> stops the loop immediately after a certain condition

#(1)
"""i=1
while i<=5:
    print(i)                 
    i+=1                     # here i+=1 is done prior of checking "if" condition, so by the time it prints 2, i becones 3 just after(due to i+=1 before if) , and the loop stops at i==3, hence it only prints 1 and 2 , inspite of i being 3
    if i==3:
        break
print("Loop ended at i=",i )
print(i)"""

#(2)
"""p=1
while p<=5:
    print(p)                
    if p==3:                 # here p+=1 is after the if condition so it first prints p , check value of p and then increases. So at p==3, it prints(p) , then (rather than increasing it to 4), checks the "if" condition and breaks after that 
        break
    p+=1
print("Loop ended at p=",p)
print(p)"""

#(3)
# Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)


"""num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the value you want to search : "))
idx=0
while idx < len(num):
    if (num[idx] == x):
        print("Value found at index", idx)
        break
    else:
        print("Value not found,Finding.....")
    idx+=1
print("End of list")"""

#(B): Continue-> skips in simple terms. terminates the ongoing loop on ground of some conditions and continues again 

#(1) : Skipping 3
"""i=0
while i<=5:
    if(i==3):
        i+=1
        continue                   # when i will be 0 it will print normally. When i==3 it will add 1 to it and again i==4 will be checked and cotinue to print. only when i==3 , it will satisfy the if condition and i will become 4 and continue the iteration, as no funtion after continue will be executed when i==3.
    print(i)    
    i+=1"""

#(2): Print only odd numbers from 1 to 100

"""i=0
while i<=100:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1"""

#(3): Print only even numbers from 1 to 100

"""i=0
while i<=100:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1"""


# For loops in python : There are used to travel through elements (check them or print) of a list , tuple or string .

#(A): Examples:

"""nums=[1,2,4,3,5,6,9]
for val in nums:              # val is a random variable representing each element individually in list
    print(val)  """              # it will print all the elements of nums list in the same order as of the list (val represent each element, we can further apply condition on "for " loop )

"""s="ApnaCollege"
for val in s:
    #print(s)                    # prints "ApnaCollege" as many times as there are characters in it which is 11          
    print(val)  """ 

#(B): Difference 

# using "for" loop
"""fruits=("mango","banana","apple","watemelon","litchi")
for a in fruits:
    print(a)
print("End of for loop")

# using "while" loop
vegitables=("onion","carrot","potato","brinjal","ladyfinger")
i=0
while i<len(vegitables):
    print(vegitables[i])
    i+=1
print("End of while loop")"""

#(3): Conditions on "for" loops

""""standard=[1,2,3,4,5,6,7,8,9,10,11,12]
for classes in standard:
    if(classes%2!=0):
        classes+=1         
        continue
    print(classes)
    classes+=1 """                # Prints only even classes

#(4): A nice problem:

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]"""

# Using while loop
"""nums=[2,7,11,15]
target = 9
i=0
while i<len(nums):
    j=i+1
    while j<len(nums):
        if(nums[i]+nums[j]==target):
            print([i,j])
            break
        j+=1
    i+=1"""

# Using for loop
"""nums=[2,7,11,15]
target = 9
for i in nums:
    j=i+1
    for j in nums:
        if(nums[i]+nums[j]==target):
            print([i,j])"""
            
# ====Question Practice==== #

#(Q1) : Print elements in the following list using a loop : [1,4,9,16,25,36,49,64,81,100]

"""squares=[1,4,9,16,25,36,49,64,81,100]
for nums in squares:
    print(nums)"""

#(Q2) : Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

"""squares=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number you want to search : "))
for nums in squares:
    if(nums==x):
        print("Number found at index->",squares.index(x))
        break
    else:
        print("Value not found. Finding..........")"""

# Alt approach:
"""nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number you want to search : "))
i=0
for el in nums:
    if(el==x):
        print("Number found at index->",i)
    i+=1"""

#================== Range()==================#

"""print(range(5))"""

# Different ways of using range

"""x=range(5)
for el in x:                            # USING STARTING VAL AND STEP IS COMPLETELY OPTIONAL. BY DEFAULT THEY ARE SET AS 0 AND 1 RESPECTIVELY
    print(el)

for p in range(5):                      # range(stoping val), ending value doesn't get printed
    print(p)

for m in range(0,6):                    # range(starting val, stopping val)
    print(m)

for n in range(0,10,2):                 # range(start,stop,step)
    print(n) """                          

# Printing of even number from 0 to 100

"""for el in range(0,100,2):
    print(el)   """                                # to include 100 also range(0,101,2)

#===================== Question Practice: =====================#

#(Q1): Using for and range() print numbers from 1 to 100

"""for nums in range(1,101):                 # if not assigned value it will take it as 1
    print(nums)"""

#(Q2): Print numbers from 100 to 1

"""for nums in range(100,0,-1):                            # withot the stepsize , dfault is (+1) hence it will not print anything starting from 100 and ending at 0
    print(nums)"""

#(Q3): Print the multiplication table of a number n upto 10 times:

"""n=float(input("Enter your number: "))

for i in range(1,11):
    print(n*i)
print("End of table")"""

# Pass Statement: If we wan to create a loop or a conditional statement and keep it blank we can't execute further function . Hence we use pass statement

"""i=0
while i<=77:                       # we can't leave loops blank and do next work


print("Next world")-------->error"""

"""for i in range(10):


print("Hola)-------------> error"""

"""a=10
b=9

if a==b:

print("Hello")----------->error"""

# With pass statement

"""i=0
while i<=77:
    pass                      

print("Next word")"""


#=================Questions===================#

#(Q1) : WAP to find the sum of first n numbers(using while):

"""print("=============Sum of first n natural number====================")
n=int(input("Enter number(n): "))
sum=0
i=0
while i<=n:
    sum+=i
    i+=1
    
print("Sum of first 'n' natural number is->",sum)"""

#(Q2) : WAP to find the factorial of first n natural number(using for):

"""print("============Factorial of first n natural number============")

n=int(input("Enter number(n): "))
factorial=1
for i in range(1,n+1,1):
    factorial*=i
>>>>>>> 2a93e30f2786d5dd7afc8fccd2d3532927786842
print("Factorial of 'n' natural number->",factorial)"""