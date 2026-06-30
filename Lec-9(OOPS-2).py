#--------------The ' del' keyword-------------------#

"""class Students:
    College_name="ABC"                             # this is a class attribute , can be called for all object tags
    def __init__(self,name,age):
        self.name=name                             # this is object attribute
        self.age=age

s1= Students("Amit",19)
print(s1.College_name)
print(s1)
print(s1.name)
print(s1.age)

del s1.name

s1.name="Adarsh"
print(s1)
print(s1.College_name)
print(s1.age)
# print(s1.name)                                        # this will give Attribute error as we have alrady deleted s1.name so there no object for obj tag s1.name

s1.name="Adarsh"
print(s1.name)                                         # This will print 'Adarsh' as we have reassigned an object to object tag s1.name after deleting 

del s1""" 

# print(s1.College_name)                                  #  These all will give name error as we have deleted the entire object tag 
# print(s1)                                               # to get these we have to re-assign object tag s1 to class as before
# print(s1.name)
# print(s1.age)

#----------------Private(like) attribute and Methods(Encapsulation)-------------------#

# All the attributes we have defined so far are public attributed , anybody can access the data by print() outside the class via creating a object tag s1,s2 etc.

#(a): Public 

"""class Account:
    def __init__(self,acc_no,acc_password):
        self.acc_no=acc_no                             # public attribute, anyone can access these info
        self.acc_password=acc_password

p1 = Account(12345,"ABCD")
      
print(p1.acc_no)                                      # these all can be easily printed and sensitive data can be seen
print(p1.acc_password)"""

#(b): Private

"""class Account:
    def __init__(self,name,acc_no,acc_password):                      # actually this is name manglingg
        self.__acc_no=acc_no                                          # we have made this private by adding two(_) in front of the obj.attribute.
        self.__acc_password=acc_password
        self.name=name                                                # now it can't be accesed outside the class . It can only be called inside the class by a method and cam be printed if the method allows

    def show_pass(self):
        print("Welcome",self.name)
        print("Your request of showing password is in process....")   # Now the account password can only be seen by calling this function(method) and following the steps   
        x=int(input("Enter your ID: "))
        y=int(input("Enter Your Account no: "))
        if x==1111 and y==self.__acc_no:
            print("Your acc password is-> ",self.__acc_password)
        else:
            print(" Wrong ID or Account no!!.\n Try Again.......")


p1 = Account("Karan",12345,"ABCD")    

# print(p1.acc_no)
# print(p1.__acc_no)                             # all of these will give attribute Error. we can't access the data(object) outside the class Account
# print(p1.acc_password)
# print(p1.__acc_password)

# to know the password we have to call the show_pass method

p1.show_pass()"""                                 # method show_pass has per-defined withing the class to print the password. hece we can only see the password by this.
# if we haven't defined any method to print the password we could have never printed the password or acc_no by print(p1.__acc_no)

#(c): Name Mangling : python does not actually hides the object. it actually renames the obj.attribute so that we can get the objects(data) by traditional
# print(obj.attribute), But it we can somehow know the mangled or changed name of the obj attribute we can print the object(data) by the traditional print method

"""class Account:
    def __init__(self,name,acc_no,acc_password):               # by adding teo(_) we are basically stopping accidental leakage of data. its not complete protecton       
        self.__acc_no=acc_no                                   # self.__acc_no-->   self._Account__acc_no      , here Account is the class name, it can be anything      
        self.__acc_password=acc_password                       # self.__acc_password--> self._Account__acc_password
        self.name=name

p1=Account("Arjun",1234,"ABC")

# print(p1.__acc_no)
# print(p1.__acc_password)                      # these will give error as always

print(p1._Account__acc_no)                       # these will give actual data as we have used the mangled name
print(p1._Account__acc_password)"""

#(d): We can also create private methods and tie it up with another method for more security

"""class Account:
    def __init__(self,name,acc_no,acc_password):                     
        self.__acc_no=acc_no                                          
        self.__acc_password=acc_password
        self.name=name                                                

    def __show_pass(self):
        print("Welcome",self.name)
        print("Your request of showing password is in process....")   
        print("Your acc password is-> ",self.__acc_password)
    
    def show_real_pass(self):                                 # the call of the method and its actions are stored in another method which is public, so calling this method will execute the work of the prior method
        self.__show_pass()

p1=Account("Alice",1234,"XYZ")

# p1.show_pass()                       # this will now give error as its alo hidden
p1.show_real_pass()                    # this is an extra layer of security

p1._Account__show_pass()"""            # again this can be accesed through mangled name

#-------------------Inheritance-----------------------#

#(a): wiithout inheritance:

"""class ToyotaCar:
    def __init__(self,name):
        self.name=name
    def car_start(self):
        print(self.name,"-Car started.........")
    def car_stop(self):
        print(self.name,"-Car stopped.........")
    def car_brake(self):
        print(self.name,"-Automatic brake pulled in case of emergency")
    
c1=ToyotaCar("Fortuner")
c1.car_brake()
c1.car_start()
c1.car_stop()                                               # we are writing the same code over and over again.

class TataCar:
    def __init__(self,name):
        self.name=name
    def car_start(self):
        print(self.name,"-Car started.........")
    def car_stop(self):
        print(self.name,"-Car stopped.........")
    def car_brake(self):
        print(self.name,"-Automatic brake pulled in case of emergency")

c2=TataCar("Nano")
c2.car_start()"""

#(b): with inheritance

"""class Car:
    def __init__(self,name):
        self.name=name
    def car_start(self):
        print(self.name,"-Car started.........")
    def car_stop(self):
        print(self.name,"-Car stopped.........")
    def car_brake(self):
        print(self.name,"-Automatic brake pulled in case of emergency")

class ToyotaCar(Car):
    # def __init__(self,name):                   # we don't even need to write this, If we will use then we must not change the parameters, like there should be self.name
    #     self.name=name                         # when we do class=ToyotaCar(Car), everything in class car comes to toyotaCar, so we don't need to do anything else
    pass

car1=ToyotaCar("Fortuner")
car1.car_start()
car1.car_stop()

class TataCar(Car):
    pass
car2=TataCar("Tata_Nano")
car2.car_start()
car2.car_stop()"""

#------Types of Inheritance-------#

# (A): Single Inheritance: 
# It is what I was doing before

#(B): Multilevel Inheritance : 

"""class Car:
    def __init__(self,name):                                           # as we have used sel.name here we must use this object attribute in all th child class or simply just pass
        self.name=name
    def car_start(self):
        print(self.name,"-Car started.........")
    def car_stop(self):
        print(self.name,"-Car stopped.........")
    def car_brake(self):
        print(self.name,"-Automatic brake pulled in case of emergency")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.name=brand                                            # we can take any parameter but we must take the same object attribute(self.name) as we have used it in parent class

class Fortuner(ToyotaCar):                                         # this is an example of multi-level inheritance
    def __init__(self,model_no):
        self.name=model_no

c1=Fortuner("Hx31_Bentec")
c1.car_start()"""

# Multiple Inheritance:

"""class A:
    varA = "Welcome to sec A"

class B:
    varB = "Welcome to sec B"

class C:
    varC = "Welcome to sec C"

class child(A,B,C):
    var = "All sections covered"

c1= child()                                      # the child class inherits the properties of multiple parent class(A,B,C)
print(c1.varA)                                   # we can also define constructors for all the parent class but name should be different 
print(c1.varB)
print(c1.varC)
print(c1.var)"""

# The super() method:

# Case-I

"""class Car:
    def __init__(self,name):                                           # as we have used sel.name here we must use this object attribute in all th child class or simply just pass
        self.name=name
    @staticmethod
    def car_start():
        print("-Car started.........")
    @staticmethod
    def car_stop():
        print("-Car stopped.........")
    @staticmethod
    def car_brake():
        print("-Automatic brake pulled in case of emergency")

class ToyotaCar(Car):
    def __init__(self,type):
        self.type=type                                           # we can take any parameter but we must take the same object attribute(self.name) as we have used it in parent class

c1=ToyotaCar("Electric")
# print(c1.name)                     # -------------------> Error as there is only one parameter in toyota car
print(c1.type)"""                       # this will run as the child class has one attribute self.type. To get self.name we have to rewrite it

# Case-II

"""class Car:
    def __init__(self,name):                                           # as we have used sel.name here we must use this object attribute in all th child class or simply just pass
        self.name=name
    @staticmethod
    def car_start():
        print("-Car started.........")
    @staticmethod
    def car_stop():
        print("-Car stopped.........")
    @staticmethod
    def car_brake():
        print("-Automatic brake pulled in case of emergency")

class ToyotaCar(Car):
    def __init__(self,type,name):
        self.type=type
        self.name=name                 # we have created another attribute self.name and hence it will run.
                                       # but we are are basically repeating as self.name is already in parent class                        

c1=ToyotaCar("Electric","Fortuner")
print(c1.name)                     
print(c1.type)"""                          # this will now give no error

# Case-III : The Super() Method

"""class Car:
    def __init__(self,name):                                           # as we have used sel.name here we must use this object attribute in all th child class or simply just pass
        self.name=name
    @staticmethod
    def car_start():
        print("-Car started.........")
    @staticmethod
    def car_stop():
        print("-Car stopped.........")
    @staticmethod
    def car_brake():
        print("-Automatic brake pulled in case of emergency")

class ToyotaCar(Car):
    def __init__(self,type,name):                     # here we have created an perameter name but has not created attribute self.name as it is already in parent class    
        self.type=type
        super().__init__(name)                        # the super(). basically fetches the method from parent class in oder to promote(DRY)                   
        super().car_start ()                          # automatically fetches the method from parent class and starts the car as we do interpretation call the class
                                                      # basically it reduces repitation

c1=ToyotaCar("Electric","Fortuner")
print(c1.name)                    
print(c1.type)"""

# Class Operator : Changing oujects of a class attribute

#Case-I: Changing class data by changing object attribute data(fail)

"""class Person:
    name = "Unknown"
    def __init__(self,name):
        self.name = name

p1 = Person("Rahul")
print(p1.name)                  #----------------> This will give Rahul
print(Person.name)"""           #-----> This will still give unkown, So the class attribute(DNA) is not changed, rather a new object attribute is created as self.name in which the argument(name) is Rahul

#Case-II: Changing obj,att in a non __init__ function:

"""class Person:
    name = "Unknown"
    def change_name(self,name):
        self.name = name

p2=Person()
p2.change_name("Rahul")
print(p2.name)
print(Person.name)"""

#Case-III : Actually changing the class attribute:

#(a)
"""class Person:
    name = "Unknown"
    def change_name(self,name):
        Person.name = name                    # so here basically we are changing the class attribute name to an argument which will be stored in place of name name parameter
    @staticmethod
    def age(a):
        print("Age = ",a)


p2=Person()
p2.change_name("Rahul")

print(p2.name)                  # object attribute name is also rahul 
print(Person.name)              # we have also changed the class attribute (name) to Rahul 

Person.age(21)                  # A static method can be called by bot class. or idedentifier.
p2.age(21)                      # a static method is basically a method in the blueprnt which can see the attributes(features) inside a n object, it can be called by the object or the class as an optional feature in the object
print(p2)                       # "<__main__.Person object at 0x000001ACCAF18C20>" , this is the location in the memory where the class object(Object created on the bluprint of Person Class) which is pointed by p2 is stored
print(id(Person))               # objects are invisible but p2 is pointing towards the object. The address of the object (0x000001ACCAF18C20)
                                              # is called the reference of the object.

print(id(Person))"""               # this is the reference of the whole class. Id gives its location

# line 346-352 is off topic here
#---------------------------------------------------------------------------------------------------------------------
#(b): Another way of changing a class attribte

"""class Person:
    name = "Unknown"
    def change_name(self,name):
        self.__class__.name = name                    # this also changes the class name tied to a object. so for a specific object identifier we can access its class          
    # @staticmethod                                   # python checks which class is tied to a specific objects abd then is the attribute we are trying to change is a class attribute    
    # def age(a):                                     # then it changes the class attribute
    #     print("Age = ",a)


p2=Person()
p2.change_name("Rahul")

print(p2.name)                  
print(Person.name)

#----------------------------------------------------------------------

class Person:
    name = "Unknown"
    def change_name(self,name):
        self.__class__.age = name                      # if we change the class attributes name which is not present in the blueprint (name->age)
    # @staticmethod                                    # python will make both name same what written in class attribute. It will not change the name of the class attribute
    # def age(a):                                     
    #     print("Age = ",a)


p2=Person()
p2.change_name("Rahul")

print(p2.name)                  
print(Person.name)"""

# Case-IV : Class Methods-> Directly accessing class attribute by a function

"""class Person:
    name="Unknown"
    @classmethod                        # updates class level attribute. cls is a required parameter like self in instance method
    def change(cls,name):               # cls is a required parameter, , we have to use class name to call the function if we hav dfined name in constructor
        cls.name=name                    # updates class attribute having the second parameter name. 

s1=Person()

s1.change("Rahul")
print(s1.name)                                 

Person.change("Rahul")
print(Person.name)"""                  # Both will give Rahul

#----------------------------------------------------

"""class Person:
    name="Unknown"
    @classmethod                      
    def change(cls,name):               # by cls.name we are basically accessing a class attribute named (name) , cls is the parameter to access class as self to access object identifier
        cls.age=name                    # if we use a non present class attribute, the class attribute name will remain unknown

s1=Person()

s1.change("Rahul")                             # it will give Unknow as the class name is still Unknown
print(s1.name)                                 

Person.change("Rahul")
print(Person.name)"""                          # both will give unknown

#--------------------------------------------------------

"""class Person:
    name="Unknown"
    def __init__(self,name1):
        self.name1=name1
    @classmethod                      
    def change(cls,name):              
        cls.name=name                    

s1=Person("Pramit")

print(s1.name)

print(s1.name1) 

s1.change("Amit")
print(s1.name)

Person.change("Rahul")

print(Person.name)""" 

# The @property decorator:
# Calculating the percentage of PCM of a student

#Case-I : Without property decorator and instance method

"""class Students:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"        # calculting percentage

s1=Students(91,85,90)

print(s1.phy)
print(s1.percentage)                      # prints the percentage based on entered attribute
                                          # if we want to change the marks of a subject % will not change

s1.phy=95
print(s1.phy)
print(s1.percentage)"""                      # marks of phy changed but % didn't , as it solves for stale data not dynamic data

# Case-II : With instance method

"""class Students:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        
    def calc_p(self):                         # a instance function, calculates %
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%" 


s1=Students(91,85,90)

print(s1.phy)
s1.calc_p()
print(s1.percentage)                      
                                          
s1.phy=95
print(s1.phy)

print(s1.percentage)           # prints the previous % inspite of changing the marks as we haven't called the method yet

s1.calc_p()                    # this updates the new % based on new marks
print(s1.percentage)

s1.maths=98
s1.calc_p()
print(s1.percentage) """          # In this method we have to call the function everytime we change marks to get modified percentage

#Case-III : Using @property decorator

"""class Students:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    @property    
    def percentage(self):                                        # we have used the property decorator . should use percentage(self) to print (s1.percentage)
        return str((self.phy + self.chem + self.maths)/3) + "%" 


s1=Students(91,85,90)                    # this is called instantiation (off topic)

print(s1.phy)                   
print(s1.percentage)                 
                                          
s1.phy=95
print(s1.phy)                            # now we don't need to call a function everytime we change marks
print(s1.percentage)                     # percentage automatically changes every time we change marks

s1.maths=98
print(s1.percentage)"""

# Runtime Polymorphism: Operator overloading : When a single operator performs multiple operations based on different context.

#Case-I: The (+) operator performs different operetions in different situations

"""print(1+4)                             # here (+) operator performs sum(adds intigers or floating values)

print("Hello" + "World")               # here (+) operator concatenates strings

print([1,2,3]+[5,6,7])"""                 # here (+) merges lists

# So (+) operator does various distinct jobs depending on the context in which it is used. This wan an example of python's implicit operator overloading.
# we can also define overloading for our own class

# Case-II
# Creating our own class of Complex no:(like class int,float, etc)

#Eg_1
"""class Complex:                                                    # Complex no in form: (a+ib) 
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def show_num(self):                         
        print(self.real, "+", "i", self.imaginary, sep="")
    def add(self, num2):                                                      # with a normal instance method 
        newReal = self.real + num2.real
        newImg = self.imaginary + num2.imaginary                 
        return str(newReal) + "+i" + str(newImg)
    
num1 = Complex(1,5)
num1.show_num()

num2=Complex(8,4)
num2.show_num()

num3=num1.add(num2)                              # for every addition we have to call the addition instance method
print(num3)"""

# num3=num1+num2                     #----------------> Error, we haven't defined + operator for our specific class, so python doesn't know what to do with (+)
# num3.show_num()                    #----------------> This will also give error as we have only defined return and not complex no

#Eg_2:
"""class Complex:                                                    # Complex no in form: (a+ib) 
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def show_num(self):                         
        print(self.real, "+", "i", self.imaginary, sep="")
    def add(self, num2):                                                    
        newReal = self.real + num2.real
        newImg = self.imaginary + num2.imaginary                 
        return Complex(newReal,  newImg)              # the result of this is used as parameter for constructr in complex class we have created
                                                      # here the newReal and newImg is used as a parameter again in complex no
                                                      # hence we can call the show_num function on the new added complex no
num1 = Complex(1,5)
num1.show_num()

num2=Complex(8,4)
num2.show_num()

num3=num1.add(num2)                              # for every addition we have to call the addition instance method, like as a.__add__(b)
print(num3)                                      # this will now give the memory location for num3 as we have put the new results as parameters again in Complex no
num3.show_num()"""                                  # this will now give the complex no after addition as we as put the result of the sum again inside the complex no

#Eg_3: So that we don't have to call the instance function. Here we will define the logic of (+) operator for our specific complex class .

"""class Complex:                                                    # Complex no in form: (a+ib) 
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def show_num(self):                         
        print(self.real, "+", "i", self.imaginary, sep="")
    def __add__(self, other):                                                  # __add__ is a predefined dunder method which let us define the logic of (+) operator
        return Complex(self.real+other.real, self.imaginary+other.imaginary)   # so that we get the result no by show_num , this is the logic of (+) operator in our class        
    def __sub__(self, other):                                                  #__add__ is a predefined dunder method which let us define the logic of (+) operator
        return Complex(self.real-other.real, self.imaginary-other.imaginary)                                                   
        
    
num1 = Complex(1,5)
num1.show_num()

num2=Complex(8,4)
num2.show_num()

# num3=num1.add(num2)                             # now we don't need to do this, we can simply use the + method
num3 = num1+ num2
print(num3)                                       # this will show the memory location of num 3
num3.show_num()

num3 = num1- num2                               # this is operator overloading ,we have defined the (+) and (-) operator as we wanted not in the traditional way
num3.show_num()"""

#---------------------Questions-------------------------#

#(Q1): Qs. Define a Circle class to create a circle with radius r using the constructor.Define an Area() method of the class which calculates the area of the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle

"""from math import pi                           # importing pythons inbuilt pi,(we can also do import math and then use math.pi)

class Circle:
    def __init__(self,r):
        self.radius=r

    def Area(self):
        print(pi*(self.radius**2))
        
    
    def Perimeter(self):
        print(2*pi*(self.radius))
        

c1=Circle(10)
c1.Area()
c1.Perimeter()"""


# Alt approach
"""from math import pi

class Circle:
    # r=int(input("Enter length of radius: "))

    def __init__(self,r):
        self.radius=r

    def Area(self):
        print("Area of Circle = πr²-->",end=" ")
        print(pi*(self.radius**2))
        
    
    def Perimeter(self):
        print("Perimeter of Circle = 2πr--> ",end=" ")
        print(2*pi*(self.radius))
r=int(input("Enter length of radius: "))
c1=Circle(r)
c1.Area()
c1.Perimeter()"""

#(Q2): Define a Employee class with attributes role, department & salary. This class also has a show_details method().Create an Engineer class that inherits properties from Employee & has additional attributes : name and age

"""class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def show_details(self):
        print("Role of individual-> ",self.role)
        print("Department of individual-> ",self.department)
        print("Salary of individual-> ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","80,000")                               # filling out the parameters of Employee class so that it can shoe details,same for all
        # super().show_details()                                                 # we do not nedd to call super here as it will get automatically passed due to obj parameter

    def Show_details(self):
        print("Name of individual-> ",self.name)
        print("Age of individual-> ",self.age)
        super().show_details()                                             # calling it here so that everything gets printed here after we print Show_details , without calling show_details



e1=Engineer("Amit",29)
e1.Show_details()"""

#(Q3):Create a class called Order which stores item & its price.Use Dunder function __ gt_( ) to convey that: order1 > order2 if price of order1 > price of order2

"""class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
   
     
    def __gt__(self,other):                                                 # we are defining our own logic of > operator
        if self.price>other.price:
            print(self.item,"is costly than",other.item)    
        elif self.price<other.price:
            print(other.item,"is costly than",self.item)
        else:
            print(self.item,"is of same cost as",other.item)
        
ord1=Order("Chips",100)
ord2=Order("Cold Coffee",70)

calc=ord2>ord1"""                                                          # we have already definied our own logic of > operator

# OOPS in a nutshell:

"""class Human:
    #  CLASS ATTRIBUTE (Universal DNA Trait)
    # Every human born from this DNA blueprint automatically shares this value.
    species = "Homo sapiens"

    #  THE INITIALIZER / CONSTRUCTOR (The Assembly Line Worker)
    # It takes the blank body (self) and installs the unique features.
    def __init__(self, name, hair_color):
        #  INSTANCE ATTRIBUTES (Dynamic Features)
        # These are unique to each individual object box.
        self.name = name                 # Assigned from the 'name' parameter
        self.hair_color = hair_color     # Assigned from the 'hair_color' parameter

    #  METHOD (An action button on the object's control panel)
    def speak(self):
        print(f"Hi, my name is {self.name} and I am a {self.species}.")                # the f string method


# --- RUNNING THE CODE IN THE RAM WAREHOUSE ---

# 1. We pass arguments ("John", "Brown") into the factory to stamp out an object.
# 2. 'j1' is our identifier (nickname/pointer label) on our desk.
j1 = Human("John", "Brown")

# 3. We create a sibling object with a different dynamic feature (parameter value).
j2 = Human("Sarah", "Red")

# Accessing the individual features (Attributes)
print(j1.hair_color)  # Output: Brown
print(j2.hair_color)  # Output: Red

# Accessing the universal trait (Class Attribute)
print(j1.species)     # Output: Homo sapiens
print(j2.species)     # Output: Homo sapiens

# Pushing the action button (Method)
j1.speak() """           # Output: Hi, my name is John and I am a Homo sapiens.
