# Lists In Python

        # (A)

"""marks=[52,4,15,12,6]
print(type(marks))
print(marks[0])
marks[4]="Sumit"
print(marks[4])
marks[0]=18
print(marks)"""

        #(B)

"""student=["Karan", "Sumit", "Aman", 85]            # Different data types are allowed in asingle list
student[0]="Arjun"
student[3]="No name"
print(student)
print(student[3])
print(student[0])                                            
print(len(student))"""                                # Length of list = no. of elements (seperated by comma) (not no of characters)


# List Slicing (almost similar to list slicing)

"""list=[45,78,65,"Arka",77,12,"Adarsh"]
print(list[0:5])
print(list[1:99])
print(list[1:])
print(list[:99])
print(list[:4])
print(list[0:len(list)])
print(list[-4:-1])"""


# List methods

#marks=[2,1,8,1,14,27,]
#marks.append(10)
#print(marks.append(10))                      # Added 10 twice at end of original marks list
#print(marks)
#print(marks.sort())
#print(marks)
#marks.sort(reverse=True)
#print(marks)
#marks.reverse()                              # Works on the final marks after the above methods are applied
#print(marks)
#marks.insert(2,"eight")                      # Works on the final marks after the above methods are applied , insert(index,element)
#print(marks)
#marks.remove(14)                              # remove 27 (the element , not index)
#print(marks)       
#marks.pop(3)                                 # Removes the element at index 3 (which is 2 after all those above methods )
#print(marks)                              



"""list=["banana","apple","litchi","mango"]
list.sort()                                              # Sorts by alphabetical order
print(list)
list2=["a","d", "m", "p", "14"]                           # here "14" is also a string hence it is give first priority in alphabetical order( here last as it is in descending order)
list2.sort(reverse=True)
print(list2)
list3=[4,8,45,78,"c"]                                      # Error can't combine strings and intigers
list3.sort()
print(list3)"""



# Tuples
         #(A)

"""tup1=(22,48,"Aman",25)
print(type(tup1))
print(tup1)
tup2=()                 
print(type(tup2))
print(tup2)
tup3=(19)
print(type(tup3))
tup4=(19,)
print(type(tup4)) """   # tuples also have slicing and indexing just like list and strig


            #(B)

"""tup1=(22,48,"Aman",25)
tup1[0]=4
print(tup1)"""           # tuples are immutable just like strings and unlike list . so we can't assign a new value to any index


# Tuple Methods

"""tup=(1,45,7,9,7,8,9)
print(tup.count(7))
print(tup.index(1))  """            # both are (element) , not index



# === QUESTION PRACTICE ===

#       (Q1)

"""print("List of favourite movies")
m1=input("Enter the name of your most favourite movie: ")
m2=input("Enter the name of your secondmost favourite movie: ")
m3=input("Enter the name of your thirdmost favourite movie: ")
list=[m1,m2,m3]
print("List of your favourite movies=>",list)"""

# Another approach :

"""list=[]
movie=list.append(input("Enter 1st movie: "))
movie=list.append(input("Enter 2nd movie: "))
movie=list.append(input("Enter 3rd movie: "))
print(list)"""

########      (Q2)                           ===  IMP QUESTION ===
"""list = [1,2,3,2,2]                               # can also be :list = ["m","a","a","m"]
c=list.copy()
c.reverse()                                      # Save the copy of the list in a variable and reverse the copy not the original list. Then compare the copy variable with the original list
if(list==c):
    print("The list is a palendrome")
else:
    print("The list is not a palendrome")"""
    



#       (Q3)  

"""print("Grade calculator of no of students")
tup=("C","D","A","A","B","B","A")
print("No of students who got grade A =>",tup.count("A"))"""


#       (Q3)
"""print("Sorting of grades from A to D")
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)"""