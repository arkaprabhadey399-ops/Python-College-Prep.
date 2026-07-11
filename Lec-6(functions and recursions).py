#======================== FUNCTIONS=============================#

# Use of functions :

#----------WITHOUT FUNCTION----------#
"""a=10
b=14
sum=a+b
print(sum)

# More lines of codes

a=13
b=15
sum=a+b
print(sum)

# More lines of codes

a=17
b=22
sum=a+b
print(sum)

# More lines of codes

a=1
b=4
sum=a+b
print(sum)

# More lines of codes

print(sum)"""                                  # This is messy and non effective way as here we are repeating same thing over and over again(redundant)

#--------USING FUNCTION--------#

"""def num_sum(a,b):                           # here we have defined the function. The name of the function is "num_sum" . a & b are called parameters whose values can be anything.
    return a+b                              # returns decides which work the function will do with parameters, like [(a+b),(a*b),(a-b),(a/b) etc..] 

print(num_sum(1,5))                         # this is called calling a function . by print we are printing the value of the function with a=1 and b=5. 1 & 5 are called arguments (which are used in place of parmeters)

# more lines of codes

print(num_sum(6,8))                        

# more lines of codes

print(num_sum(22,11))                        

# more lines of codes

print(num_sum(222,789)) 

# more lines of codes

print(num_sum(122,0))                        

# more lines of codes

print(num_sum(1001,58))                   # by already defying the fuction and calling it every time . we are saving same and time and that's what good programmers do, avoid repeatation

# more lines of codes"""

# Two types of defying a sum function:

#(A)
"""def sum_nums(a,b):                          #-----------defying the function , name of the function is sum_nums
    p=a+b
    print(p)                                # don't do print(p) after return p
    return(p)
    
sum_nums(21,14)                             # Calling the function
sum_nums(78,100)"""

#(B)
"""def val(a,b):            
    return(a+b)

print(val(1,2))                            # Here as we have not defined print, in the original function so we have to use print while calling the function to print value
print(val(1,5))
print(val(88,2))
print(val(12,42))
print(val(147,112))"""

# what the return does in a function.
#the return function stops the the func apperently and returns the work or value assigned to it to the comp memory. to see it we have to print the function call or include a print statement in the function

"""def menu(a,b):
    return "cheeseburger"

my_lunch=menu("burger","cheese")
print(my_lunch)"""

# Function without parameters':
#(A):
"""def func():

    return "Hello"                 # this is called output we can also define a function without it

func()                             # calling the function, this will not print anything as we have not used print here . the output will be Hello but it will not get printed 
print(func())"""

#(B):
"""def funct():                       # this function will always print hello but not give any output as we have not mentioned return
    print("Hello")                 # this itself will print hello

funct()
print(funct())"""                   # it will give none as we have not defined return. so it will ony always print "Hello " if we call it
                                    # Here hello is printed twice but acc to me it should have been printed once and then none. Actuall in funct()--> hello gets printed and print(funct())--> Hello ad none gets printed because before executing print(--) python sees inside funct() and prints it then it sees the function do no have any return defined so it gives print(--) as none
#(C):
""""def functi():
    a="Hello"
    print(a)                       # this function will both print and return Hello as output
    return a
                                   # when there is return use print(), when there is print() call the function normally
functi()
print(functi())"""       

# Question : Find the average of three numbers multiple times

"""def func_avg(a,b,c):
    sum= a+b+c
    average= sum/3
    print( average)
    return average                    # if we haven't used this it would still give value when we call func_avg but it will give value and print none for print(func_avg())


func_avg(10,5,7)
func_avg(10,105,6)
func_avg(1510,5,72)
func_avg(100,15,57)
func_avg(112,4,2)"""

# print function:

"""print("Hello world")"""                 # print is a pre-defined(built-in) function in python so every time we use it we are bascically calling the function. The text hello world is an argument. also whil use print in anoher function we are bascically using one function into another

# print is defined as sep=" " and end="\n"--> so whenever we seprate anything by comma it gives an outomatic space and whenever we end a print statement and write another, it gets printed on separate lines . to change this we have to change those

"""print("Hello","World", sep="+")"""   # Here although we have seperated them via comma there came a + instead of space as we have changed the parameter for sep in function

"""print("Hello",end="__")
print("World") """                        # Here although we have wrote hello and world on different lines it will pprint on same line as we have changed from "\n" to "__"

# Default parameters

#(A)
"""def calc_fn(a,b):
    print(a*b)
    return(a*b)

calc_fn()"""                           #--> error as we have neither called  the fn properly(haven't used argument) nor assigned default value to the parameters

#(B)
"""def calc_fn(a=5,b=2):
    print(a*b)
    return(a*b)

calc_fn()"""                             # here it will not give error as we have assigned default values to the parameters . so we may not use arguments while calling the function

#(C)
"""def calc_fn(a=5,b=2):
    print(a*b)
    return(a*b)

calc_fn(7,7)"""                         # Arguments always overwrites default values of the parameters

#(D)
"""def calc_fn(a,b=5):
    print(a*b)
    return(a*b)

calc_fn(1)"""                              # if we have assigned default parameter to any one of the parameters , we must write argument for the other

"""def calc_fn(a=6,b):
    print(a*b)
    return(a*b)

calc_fn(2)"""                           #--> ERROR , we must start assigning default values from the end parameter

# Question Practice:

#(Q1): WAP to print the length of a list. (list is the parameter)

"""def list_length(lst):
    print(len(lst))
    return len(lst)

# Example call:

heros = ["Thor","Captain America","Ironman","Hulk","Hackeye"]
list_length(heros)"""

#(Q2): WAF to print the elements of a list in a single line. ( list is the parameter)

"""def list_elements(lst):
    print(lst)
    return(lst)

# Example Call:
list_elements(["Hello",10,"String","Slicing",21,34])"""

# Alt approach:

"""heros = ["Thor","Captain America","Ironman","Hulk","Hackeye"]
places=["Noida","Delhi","Mumbai","Chennai","Mohali","Sikkim"]

def list_elements(list):
    for i in list:
        print(i, end=" ; ")
    return(i)

list_elements(heros)"""                      # I don't know why there is ; last but not in case of print(list_elements)
#print(list_elements(heros))

#(Q3): WAF to find the factorial of n.(n is the parameter)

"""def fact_calc(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)
    return result

# Example call
fact_calc(5)"""

#(Q4): WAF to convert dollar($) to INR(₹)

"""def currency_convert(usd_val):
    inr_val=usd_val*94
    print(usd_val,"USD =",inr_val, "INR")
    return(usd_val,"USD=",inr_val,"INR")

#Example call:
currency_convert(4)"""

#(Q5): WAF to determine whether a number is odd or even. Print "ODD" in case of odd and "EVEN" in case of even:

"""def type_calc(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

#Example call
n=float(input("Enter your number:- "))
type_calc(n)"""

#------------RECURSION------------#

# Here we call a function inside the same function by changing the parameters. So when the function gets exected it again gets executed as its already called inside the function. We need a base case (stopping case) to stop the function.

#(A): Back counting
"""def back_count(n):                        # we have defined a function back_count with a parameter n
    if n==0:                                # this is the base case(stopping condition) 
        return 0000                        # when n will be 0,it will stop and hand over 2 to comp memory . so back_count(0) will become 2 but the fuction will stop due to return
    print(n)                              # this will print all n which are not 0
    back_count(n-1)                      # this is where recurssion will work. we have called the function inside the function itself with a parameter n-1, so while executing for ever n, the function will automatically call n-1 and will re-run again and again until base case is hit. base case will stop the function due to return

back_count(5)                          # back counting from 5 to 1
print(back_count(0))"""               # it will print 2 as we have written return 0000 for back_count(O)

#(B): without base case

# Without the base case recursion will go infinitely and ultimately give error due to stack overflow(capacity 1000)

"""def back_count(n):                       
    # if n==0:                                
    #     return 0000                        
    print(n)                             
    back_count(n-1)                     

back_count(5)  """                        

#(B): Doing work after return case:

"""def back_count(n):                       
    if n==0:                                
        return                        
    print(n)                             
    back_count(n-1) 
    print("End")                         # To lazy to write logic. logic in notes. Call stack                    

back_count(5)"""

# Factorial calculation:

"""def factorial_calc(n):
    if n==1:
        return 1                                      #If you call factorial(3), Python builds a chain of waiting math equations:factorial(3) wants to do: 3 * factorial(2) (Waiting...)factorial(2) wants to do: 2 * factorial(1) (Waiting...)factorial(1) hits the base case.If you used return 1: It hands the number 1 up the chain. The math collapses perfectly: 2 * 1 = 2, then 3 * 2 = 6. Success!If you used just return: It hands back None. Python tries to do 2 * None and crashes with a loud error: "TypeError: unsupported operand type.
    else:
        return (n*factorial_calc(n-1))

diff_val_of_n= factorial_calc(5)
print(diff_val_of_n)"""

#-------------QUESTIONS-----------#

#(Q1): write a recursive function to calculate the sum of first n natural numbers

"""def sum_num(n):
    if n==0:
        return 0
    return (n)+sum_num(n-1)


n=int(input("Enter number: "))
print(sum_num(n))"""

#(Q2): Write a recursive function to print all elements in a list. (HINT: Use list and index as parameters)

"""def print_list(group, idx):
    if idx == len(group):
        return
        
    print(group[idx])
    print_list(group, idx+1)
                                                          # alt method of slicing
val=[1,2,4,5,7,8,33,55]

print_list(val,0)"""

#(Q3): Write a function named calculate_tax(price) that takes a price, multiplies it by 0.05 (5% tax), and returns the tax amount. Ensure it doesn't print anything itself—you must call it, save the result in a variable, and print it outside the function.

"""def calculate_tax(price):
    final_price=price*0.05
    return final_price

n=float(input("Enter non taxed amount($): "))
calc=calculate_tax(n)
print("Price after being taxed-->",calc, sep=" $ ")"""

#(Q4): Write a recursive function called rocket_launch(n) that counts down from n to 1 printing each number, and when it hits 0, it prints "Blast off!" and exits. (Hint: Think about your base case and whether your return needs a number or can be alone).

"""def rocket_launch(n):
    if n==0:
        print("Blast off")
        return 
    print(n)
    rocket_launch(n-1)

n=int(input("Enter your countdown time(sec): "))
print("Rocket launching in.....")
rocket_launch(n)
print("Rocket launched sucessfully !!")"""

#(Q5):  Write a recursive function recursive_sum(n) that calculates the sum of all numbers from 1 up to n. For example, recursive_sum(4) should calculate 4 + 3 + 2 + 1 and return 10. (Hint: This builds a math chain exactly like your factorial example!)


"""def recursive_sum(n):
    if n==1:
        return 1
    else:
        return n + recursive_sum(n-1)
    
n=int(input("Enter number: "))
final_sum=recursive_sum(n)
print("Sum of first",n,"natural number is -->", end=" ")
print(final_sum)"""

#%% 

# Lamda Function:

# Not using lamda function:

def square(x):
    return x*x
# print(square(5))

def radius(fx,fy):                      # passing a function as an argument. Functions can also be passed as arguments in another function
    return fx + fy

circle_rad = radius(square(4),square(3))

print(circle_rad)

#%%
# Using lamda function
# Syntax : lamda (what_it_takes): (what_it_will_return) 

square = lambda x : x*x
# print(square(7))                            

def radius(fx,valx,fy,valy):
    return fx(valx) + fy(valy)               # this is not multiply, fx(valx) is actually calling another function with parameter x like square(x)
print(radius(square,3,square,4))

# Whats actually happening :

# lamda creates an anonymous function which take a parameter : returns worked out parameter
# when we are defying radius (fx,valx,fy,valy) we are just passing some parametized temporary name and values. Actually we are trying to pass a funtion in the argument of another function.
# actually fx(valx) is infact calling that previous function with parameter valx. in turns the radius function performs operation with that previous function
# having argument valx
# we can call any fx(valx) like anything we have defined earlier , valx is a paramenter for any previous function fx


#%%

# More examples on lamda function

square = lambda x: x**2
cube = lambda y: y**3
avg = lambda x,y,z : (x+y+z)/3

def random_func(fx,x):
    return fx(x) + 6

print(random_func(square,5))                           # here we are calling the squre function with arg 5
print(random_func(cube,2))

# Now for this as there are three arg in the pervious function and only one ith new function(for that old func):
"""print(random_func(avg,(1,3,5)))"""      #----------> Type error , as a tuple is only considered as 1 arg and we need 2 more for avg function

# There is two methods of doing it :

#M-I : The astric(*) method: seperates every element of a tuple and consider them as an argument

square = lambda x: x**2
cube = lambda y: y**3
avg = lambda x,y,z : (x+y+z)/3

def random_func(fx,x):
    return fx(*x) + 6                   # now we can pass a tuple through x and it will seperate all individual elements and consider them as an argument

print(random_func(square,(5,)))        # now we have to pass singular elements as tuple also as now x only accepts tuples            
print(random_func(cube,(2,)))
print(random_func(avg,(1,3,5)))          # gives 9.0 as ans


#M-II : The data method, no need of passing argument

avg_tuple = lambda data: sum(data) / len(data)                # everything else remains completely same only avg changed

def random_func(fx, x):
    return fx(x) + 6

# This works perfectly now because avg_tuple expects a single object
print(random_func(avg_tuple, (1, 3, 5)))  # Outputs: 9.0


