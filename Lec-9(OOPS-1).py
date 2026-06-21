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

class Students:
    College_Name="ICE"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Viewing students Profile")
    def greet_student(self):
        print("Welcome!! ",self.name ,"/nYour Marks is: ",self.marks)

