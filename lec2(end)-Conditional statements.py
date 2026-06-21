<<<<<<< HEAD
# Conditional Statements 

# Using Only If

"""age=24
if(age>=18):
    print("You can vote")"""

"""age=16
if(age>=18):
    print("You can get a Driver's License ")   """            # Nothing will get printed as the condition is not fullfilled


# Using only if and elif

"""age=24
if(age>=18):
    print("You can give vote")
elif(age<18):
    print("You can't give vote")"""


"""age=16
if(age>=18):
    print("You can give vote")
elif(age<18):
    print("You can't give vote")"""


"""print("====Welcome to eligibility test====")
age=int(input("Enter your age in years: "))
if(age>18):
    print("You can vote")
    print("You can get a driver's license")
    print("Congratulation on being and adult ")
elif(age<18):
    print("You can't vote")
    print("You can get a DL but you can apply for RCC")
    print("Enjoy your childhood")
elif(age==18):
    print("You can vote if you have applied for voter card and have your voter number")
    print("You can apply for a Driver's License but first you have to apply for a Lerner's License")
    print("Congratulations on being an young adult")
print("Thank You for using our service")
print("Please rate us on a scale of 1 to 10")
rate=float(input("Please enter your rating: "))    
if (5.0 <= rate <= 10.0):
    print("Thank you for rating us well")
elif (1.0 <= rate < 5.0):
    print("Thank you for your feedback. We'll try to improve.")
elif(rate==0):
    print("We are so sorry to hear it , please provide inprovement tips")
    feedback=input("Please enter your feedback: ")
    print("Thanks for your feedback, We will definitely look into it and inpove")
else:
    print("Please enter a valid rating between 1 and 10.")
print("Thanks, Visit Again")"""

#Using if, elif and else
#Creating a grade calculator

"""print("==========WELCOME TO GRADE CALCULATOR===========")
marks=int(input("Enter your marks: "))
if(marks>=90):
    print("Grade A")
    print("Excellent. Keep it up")
elif(80<=marks<90):
    print("Grade B")
    print("Very Good. Keep inproving") 
elif(70<=marks<80):
    print("Grade C")
    print("Good. Try to inprove more next time")
elif(60<=marks<70):
    print("Grade D")
    print("Moderate. Work harder next time")
elif(0<=marks<60):
    print("Fail")
    print("Keep trying. You will succed next time. Be more attentive in class and practice mmore")
else:
    print("ERROR")
    print("Enter a valid marks between 1 to 100")
print("Thank You For using our Service")"""



# Another Grade Calculator with sligght nesting

"""marks=int(input("Enter Student's Marks: "))

if(marks>=90):
    if(marks>100):
        print("Not Possible, Please enter valid marks")
    else:
        Grade="A"
elif(marks>=80 and marks<90):
    Grade="B"
elif(marks>=70 and marks<80):
    Grade="C"
else:
    if(marks<0):
        print("Not Possible, Please enter valid marks")
    else:
        Grade="D"

print("The Grade of the Student is-> ",Grade) """          #Wrong Code



# Nesting
"""print("====Eligible Age for Driving")
age=int(input("Enter your age: "))
if(age>=18):
    if(age>=80):                                                         #Using if inside if
        print("You should not drive at this age.")
    else:
        print("You are both physically and mentally fit to drive")
elif(age<18):
    print("You are not at that age to drive")
else:
    print("ERROR! Please enter a valid age")
print("Thanks for using our service")"""


#===QUESTION PRACTICE===

#   (Q1)

"""print("Odd or Even No Identifier.")
num=int(input("Input an intiger no: "))
if(num%2==0):
    print("Your number is even")
else:
    print("Your number is odd")"""

#    (Q2)

"""print("Finding the greatest number")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))

if(num1>=num2):
    if(num1<=num3):
        print("The greatest no. among the above is-> ",num3)
    elif(num1>=num3):
        print("The greatest no. among the above is-> ",num1)
elif(num1<num2):
    if(num2>=num3):
        print("The greatest no. among the above is-> ",num2)
    else:
        print("The greatest no. among the above is-> ",num3)"""


# Better approach

"""num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))
if(num1>=num2 and num1>=num3):                      #As logical operator and is used it will only print("The greatest number is-> ",num1), when both cases are true
    print("The greatest number is-> ",num1)
elif(num2>=num3):
    print("The greatest number is-> ",num2)         # After case one only two cases remains if one of the above cases become false
else:
    print("The greatest number is-> ",num3)"""


#       (Q3)

"""print("Multiple of 7 or not!")

num=float(input("Enter your number: "))
a=int(num/7)
b=num/7
if(num%7==0):
    print("Entered number is divisible by 7")
    print("The Quotient when divided by 7 is-> ",int(num/7))
    print("So 7*",a, "=", int(num))
else:
    print("Entered number is not divisible by 7")
    print("The Quotient when divided by 7 is-> ",num/7)
    print("So 7*",b, "=", num)"""


=======
# Conditional Statements 

# Using Only If

"""age=24
if(age>=18):
    print("You can vote")"""

"""age=16
if(age>=18):
    print("You can get a Driver's License ")   """            # Nothing will get printed as the condition is not fullfilled


# Using only if and elif

"""age=24
if(age>=18):
    print("You can give vote")
elif(age<18):
    print("You can't give vote")"""


"""age=16
if(age>=18):
    print("You can give vote")
elif(age<18):
    print("You can't give vote")"""


"""print("====Welcome to eligibility test====")
age=int(input("Enter your age in years: "))
if(age>18):
    print("You can vote")
    print("You can get a driver's license")
    print("Congratulation on being and adult ")
elif(age<18):
    print("You can't vote")
    print("You can get a DL but you can apply for RCC")
    print("Enjoy your childhood")
elif(age==18):
    print("You can vote if you have applied for voter card and have your voter number")
    print("You can apply for a Driver's License but first you have to apply for a Lerner's License")
    print("Congratulations on being an young adult")
print("Thank You for using our service")
print("Please rate us on a scale of 1 to 10")
rate=float(input("Please enter your rating: "))    
if (5.0 <= rate <= 10.0):
    print("Thank you for rating us well")
elif (1.0 <= rate < 5.0):
    print("Thank you for your feedback. We'll try to improve.")
elif(rate==0):
    print("We are so sorry to hear it , please provide inprovement tips")
    feedback=input("Please enter your feedback: ")
    print("Thanks for your feedback, We will definitely look into it and inpove")
else:
    print("Please enter a valid rating between 1 and 10.")
print("Thanks, Visit Again")"""

#Using if, elif and else
#Creating a grade calculator

"""print("==========WELCOME TO GRADE CALCULATOR===========")
marks=int(input("Enter your marks: "))
if(marks>=90):
    print("Grade A")
    print("Excellent. Keep it up")
elif(80<=marks<90):
    print("Grade B")
    print("Very Good. Keep inproving") 
elif(70<=marks<80):
    print("Grade C")
    print("Good. Try to inprove more next time")
elif(60<=marks<70):
    print("Grade D")
    print("Moderate. Work harder next time")
elif(0<=marks<60):
    print("Fail")
    print("Keep trying. You will succed next time. Be more attentive in class and practice mmore")
else:
    print("ERROR")
    print("Enter a valid marks between 1 to 100")
print("Thank You For using our Service")"""



# Another Grade Calculator with sligght nesting

"""marks=int(input("Enter Student's Marks: "))

if(marks>=90):
    if(marks>100):
        print("Not Possible, Please enter valid marks")
    else:
        Grade="A"
elif(marks>=80 and marks<90):
    Grade="B"
elif(marks>=70 and marks<80):
    Grade="C"
else:
    if(marks<0):
        print("Not Possible, Please enter valid marks")
    else:
        Grade="D"

print("The Grade of the Student is-> ",Grade) """          #Wrong Code



# Nesting
"""print("====Eligible Age for Driving")
age=int(input("Enter your age: "))
if(age>=18):
    if(age>=80):                                                         #Using if inside if
        print("You should not drive at this age.")
    else:
        print("You are both physically and mentally fit to drive")
elif(age<18):
    print("You are not at that age to drive")
else:
    print("ERROR! Please enter a valid age")
print("Thanks for using our service")"""


#===QUESTION PRACTICE===

#   (Q1)

"""print("Odd or Even No Identifier.")
num=int(input("Input an intiger no: "))
if(num%2==0):
    print("Your number is even")
else:
    print("Your number is odd")"""

#    (Q2)

"""print("Finding the greatest number")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))

if(num1>=num2):
    if(num1<=num3):
        print("The greatest no. among the above is-> ",num3)
    elif(num1>=num3):
        print("The greatest no. among the above is-> ",num1)
elif(num1<num2):
    if(num2>=num3):
        print("The greatest no. among the above is-> ",num2)
    else:
        print("The greatest no. among the above is-> ",num3)"""


# Better approach

"""num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))
if(num1>=num2 and num1>=num3):                      #As logical operator and is used it will only print("The greatest number is-> ",num1), when both cases are true
    print("The greatest number is-> ",num1)
elif(num2>=num3):
    print("The greatest number is-> ",num2)         # After case one only two cases remains if one of the above cases become false
else:
    print("The greatest number is-> ",num3)"""


#       (Q3)

"""print("Multiple of 7 or not!")

num=float(input("Enter your number: "))
a=int(num/7)
b=num/7
if(num%7==0):
    print("Entered number is divisible by 7")
    print("The Quotient when divided by 7 is-> ",int(num/7))
    print("So 7*",a, "=", int(num))
else:
    print("Entered number is not divisible by 7")
    print("The Quotient when divided by 7 is-> ",num/7)
    print("So 7*",b, "=", num)"""


>>>>>>> 2a93e30f2786d5dd7afc8fccd2d3532927786842
