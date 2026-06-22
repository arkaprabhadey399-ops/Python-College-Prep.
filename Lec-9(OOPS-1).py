#-------------------Class & Objects-----------------#

#(A)

"""class Student:                                 # defying a class(blueprint) with several info
    name = "Arjun"
    age = "23"
    profession = "Freelancing"

s1 = Student()                                # s1 is the object variable. we have to assing it with a particular class(blueprint) from which we are going to, by adding parenthisis we are basically calling the constructer
print(s1)                                     # prints what is s1
print(s1.name)                                # prints the value of name in the class assigned to s1
print(s1.age)                                 # prints the value of age in the class assigned to s1
print(s1.profession)                          # prints the value of profession in the class assigned to s1

s2 = Student()
print(s2.name) """                               # This will be same as s1 as both s1 and s2 are assigned same class( "Student") and the name in student class is fixed ("Arjun")

#(B)
"""class CarM:                                         # by defing class we are making the blueprint of a carM
    colour = "Blue"
    seats = "5 seater"
    gear_type = "Gear less"
    ground_clearence = "Decent"
    top_speed = "180 kmph"
    Car_type = "SUV"

c1=CarM()                                          # c1 is a car made by the bluprints of carM
print(c1.colour)
print(c1.seats)

c2=CarM()
print(c2.colour)"""                                   # c2 will have same colour as c1 as it is made of same blueprint


#------------------------- __init__ function-------------------

#(A)
"""class Student:
    def __init__(self):                              # self refers to the object we are creating 
        print("Adding new students....")
        print(self)
s1=Student()                                         # by giving the parenthisis we are using(calling) the argument self
print(s1)                                            # both s1 and self are the same thing as we are now calling the object s1 now

s2=Student()                                         # each time by adding parenthesis we are calling again the constructor, so for every new object __init__ function will be called from begining 
print(s2)"""                                            # now s2 and self will be same but s1 and s2 are not same

#(B)
"""class Students:
    def __init__(self,Name):                          # Name is a new parameter which can be used, here multiple names can be stored
        self.name=Name                                # we have created this to add diff student name without writing a fixed name. here a info name is created for were object we call. self refers to the object that we will create. The self.name is used so that it can me printed by s1.name or s2.name like before
        print("Adding new students....")              # this will get printed for every object

s1=Students("Karan")                                  # Karan hets stored in the name (info) of the class ( just like previous but here diff names are possibe)
print(s1.name)                                        # just like before, but here there is no fixed name tab, Whats written inside the () gets stored inside the var Name which inturn gets stored in name tab(like before) so here as name = Name , multiple names are possible


# class Students:
#     name = "Karan"                                  # this is the long process and only one name is fixed here
# s1=Students()
# print(s1.name)

s2=Students("Arjun")
print(s2.name)

s3=Students("Rishav")
print(s3.name)

s4=Students("Prince")
print(s4.name)

s5=Students("Rohit")
print(s5.name)

print("Added")"""

#(C)
"""class Cars:
    def __init__(self,Brand):
        self.abcd=Brand                                       # by this we are creating a abcd tab which will have brand names
        print("Viewing Brand Name")                           # the self.abcd is taken so that every time we print(object.name) the brand name gets printed for each diff. objects

c1=Cars("TATA")
print(c1.abcd)

c2=Cars("Mercedes")
print(c2.abcd)"""

#(D)
"""class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding Student's Information.....")

s1=Students("Rishab",91)
print("(i) Name of student-->",s1.name ,"\n    Marks obtained-->",s1.marks)

s2=Students("Rahul",82)
print("(ii) Name of student-->",s2.name)
print("     Marks obtained-->",s2.marks)"""

#(E)

# Default Constructor:

"""class Students:
    name="Karan"
    age=24
    def __init__(self):                             # this is a default constructor automatically created by python whenever we create class(We don't need to write this)
        pass

s1=Students()
print("Name: ",s1.name)
print("Age: ",s1.age)"""

# Parameterised Constructor:

"""class Students:                                  # this is P.C , we create parameters according to our needs , it is not automatically created by python
    College_Name = "ABC College"                  # class attribute, same of all objects
    def __init__(self,name,age):                 # object attribute(name,age) , different for different objects
        self.name=name                            # object attribute
        self.age=age                              # object attribute
    
s1=Students("Arjun",20)
print("Name: ",s1.name)                            # these can't be written as Students.attibute , it must be written as self.attibute(s1 or s2.attribut) as they are objevt attributre
print("Age: ",s1.age)
print(s1.College_Name)                             # same for all objects
print(Students.College_Name)"""                    # can also be written as class name.attribute name(College_attribute)

#(F)
"""class Students:
    College_Name = "ABC College"                     # class attribute( same for all objects)
    name="anonymous"
    def __init__(self,name,age):
        self.name=name                               # object attribute( diff for diff objects)
        self.age=age

s1=Students("Amit",14)
print(s1.name)"""                                  # object attribute > class attribute (so for same variable(name) in both class attribute and object attribute, object attribute will always be printed)

#----------------------------Methods------------------------------#

"""class Students:
    College_Name="ICE"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Viewing students Profile")
    def greet_student(self):                                                       # we are calling this for all objects hence the first parameter must be self
        print("Welcome!!", self.name, "\nYour Marks is:", self.marks)
        return "Welcome!!", self.name, "Your Marks is:", self.marks

s1=Students("Rishabh", 88)
print(s1.College_Name)

s1.greet_student()

print("Welcome!!",s1.name)
print("Your Marks is: ",s1.marks)                         # can also be done by this

s2=Students("Pramit",77)
print(s2.College_Name)
print(s2.greet_student())"""

# QUESTIONS:

#(Q1) : Create student class that takes names & marks of 3 subjects as arguments in constructor. Then create a method to print the average .

"""class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.m1=sub1
        self.m2=sub2
        self.m3=sub3
        print("Viewing Student Profile")
    def calc_avg(self):                                                     # self is taken as first parameterr so that we can call this method for diff objects
        sum = self.m1+self.m2+self.m3
        print("Welcome!!",self.name)
        print("The average of your marks in 3 subjects are: ",sum/3)


s1=Student("Adarsh",91,97,95)
s1.calc_avg()"""

#Alt Approach:

"""class Student:
    def __init__(self,name,marks):                                          # marks of 3 sub should be in list tuple dictionary or sets
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum = 0                                                             # using Loops
        for val in self.marks:
            sum+=val
        print("Welcome",self.name,"your avg marks is",sum/3)

s1=Student("Amit",[99,98,97])
s1.get_avg()

s1.name="Rohan"                                  # we can also change any agrument for any object directly like this
s1.get_avg()"""

#---------------Static method----------------#

"""class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Adding Students")

    @staticmethod                                               # so that (object.age_valid) does not give error
    def age_valid():                                            # we haven't used self parameter in this function , so to call it for different objects we use Staticmethod
        print("You can sign petition")
    
    def info(self):
        print("Welcome",self.name,"!!")
        print("Your age-> ",self.age)

s1=Students("Aman",16)
s1.info()

s2=Students("Pawan",19)
s2.info()
s2.age_valid()                      

s3=Students("Adarsh",18)
s3.info()
s3.age_valid()

s4=Students("Lucky",16)
s3.info()"""

#---------Pilars of OOPS-----------#

#(a): Abstraction : Hiding unnessary work from user

# An Example
"""class Auto_Car:                                       # Like abstraction when a car starts the drive doesn't see the underlaying mechanisms of the car
    def __init__(self):                               # before the car starts
        self.engine=False
        self.clutch=False
        self.ignition=False
    def turn_key(self):                               # after the key is turned
        self.engine=True
        self.clutch=True                              # asuming this is an automatic car , all these processes are not seen by the the driver
        self.ignition=True
        print("Car Started...........!!")

c1=Auto_Car()
c1.turn_key()"""


#(b): Encapsulation : Wrapping data and function into a single unit(object):

#Example:
#All the codes we have written so far in this file .

"""class Students:
    def __init__(self,name,age):                             # All the data and functions are wrapped inside Students
        self.name=name
        self.age=age
        print("Adding Students")

    @staticmethod                                               
    def age_valid():                                           
        print("You can sign petition")
    
    def info(self):
        print("Welcome",self.name,"!!")
        print("Your age-> ",self.age)"""

# Questions:

#(Q1): Create account class for two attributes-balance & account number. Create methods for debit, credit and printing the balance


"""class Account:
    print("Welome to Automated Service ")
   
    def __init__(self,name,balance,account_no):
        self.name=name
        self.balance = balance
        self.account_no = account_no
        print("Hello..!!")
        print("Intialising some Information")

    def debit(self,v1):
        self.balance-=v1
        print("*Debited amount from bank-> $",v1)

    def credit(self,v2):
        self.balance+=v2
        print("*Credited amount to bank-> $ ",v2)

    def Details(self):
        
        print("=============================Your account Details:-============================ ")
        print(" Your Name-> ",self.name)
        print(" Your Account Number-> ",self.account_no)
        print(" Present amount in bank-> $",self.balance)


p1=Account("Avinash",4569,1234567)
p1.debit( 14)
p1.credit(24)
p1.Details()"""


# To be continued
