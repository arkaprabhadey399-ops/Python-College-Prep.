# Dictionary in Python

"""my_dict = {
    "Name": "Arka",
    "Age": 18,                                  # Syntax mistakes : taking (=) and not (:) after keys and not adding (,) at the end of a value in a line
    "Courses": ["Phy","Chem","Maths"],
    "Languages":("C++","Java","Python"),
    "Scores": {
        "Physics":8,
        "Chemistry":7,
        "Maths":9,
    },
    "Work": "Coding",
    99:"Marks in nothing",
    99.99: "Closet",
    ("eng","beng","eco"): "Optional subject",          # Can't take lists as 
}
print(my_dict)
print(type(my_dict))
print(len(my_dict))
print(my_dict["Name"])                           # print(my_dict["Name1"])-> error(no key named name1 present)
print(my_dict["Courses"])                        # this is same as print(my_dict.get("Courses))
print(my_dict["Scores"])      
my_dict["City"]="Delhi"                          # adds ney key "City" and assigs its value as delhi
print(my_dict)
my_dict["Age"]=21                                # changes the value of key "Age" to 21 from 18
print(my_dict)"""



# Nested dictionary 


"""info = {
    "Name": "Arka",
    "Age": 18,
    "Courses": ["Phy","Chem","Maths"],
    "Languages":("C++","Java","Python"),
    "Scores": {
        "Physics":8,                         # its like dictionary inside dictionary
        "Chemistry":7,                       # same concept ass of nesting in condditional statements
        "Maths":9,
    },
    "Work": "Coding"
}

print(info["Scores"])
print(info["Scores"]["Maths"])
print(info["Scores"]["Physics"])
print(info["Scores"]["Chemistry"])
info["Name"]="Adarsh"
info["Surname"]="Shaw"
print(info)"""


# Null Dictionary


"""dict={}
print(type(dict))
dict["Name"]="Arka"
print(dict)
dict[("Surname","Age","Place")]="Dey",18,"Delhi"            # Here the whole tuple is a single key
print(dict)
print(len(dict))"""


# Dictionary Methods


"""student = {
    "Name": "Arka",
    "Age": 18,
    "Courses": ["Phy","Chem","Maths"],
    "Languages":("C++","Java","Python"),
    "Scores": {
        "Physics":8,                         
        "Chemistry":7,                       
        "Maths":9,
    },
    "Work": "Coding",
    "Standard": 12
}

print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(len(list(student.values())))
print(student.items())
print(list(student.items()))
pairs=list(student.items())                                 # not pairs=(student.items()). always store them in a list first
print(pairs[0])
print(pairs[1])
print(student.get("Courses"))
print(tuple(student.get("Courses")))
print(student.get("Scores"))
student.update({"Work": "Study"})                            # you can't use print for this , it will give none
print(student)
student.update({"City": "Delhi"})                             # you can also add new key and values
print(student)"""


# Difference between print(student.get("Key")) and print(student["key"])


learning = {
    "Name": "Arka",
    "Age": 18,
    "Courses": ["Phy","Chem","Maths"],
    "Languages":("C++","Java","Python"),
    "Scores": {
        "Physics":8,                         
        "Chemistry":7,                      
        "Maths":9,
    },
    "Work": "Coding"
}

"""print(learning["Name"])                                  
print(learning.get("Name"))                             # both gives same answer

                         # But if we write a wrong name both will give diff. responses

#print(learning["Name2"])                #there is no name2-> key error (no code after this line will get executed)
print(learning.get("Name2"))"""            # there is no name2-> response will be "none" (all codes after this line will get executed)


# Empty Dictionary


"""dict={}
print(type(dict))
print(dict)
dict.update({"Name": "Arka"})
print(dict)"""



# SETS 


"""set1={1,2,5,8,"Hello","World",8,19,27,"Hello"}
print(set1)                                            # every time we print this the order of set will be diff. , duplicate values will only be printed once
print(type(set1))"""

# Set Methods


"""collection=set()
print(type(collection))
collection.add(1)
collection.add(1)
collection.add(2)
collection.add(27)
collection.add("Hi")
print(collection)
print(len(collection))
collection.remove(27)
print(collection)
#collection.clear()
#print(collection)                # null set will get printed
print(collection.pop()) """          # removes a/multiple random element (everytime new ) from the set . Prins only the removed element


# Union and intersection in sets

"""set1={1,2,3,6,5}
set2={2,3,6,8,9,5}
print(set1.union(set2))                       # Just like in mathametics
print(set1.intersection(set2))"""




# =======QUESTION PRACTICE========

#(Q1) : Store the following words in apython dictionary:- table : "a piece of furniture", "list of facts and figures", cat : "a small animal"
# Done alone

"""print("====Storing Values in a Dictionary====")
dictionary = {
    "table": ["a piece of furniture", "list of facts and figures"],              # whenever there is more than one value for a key save it as a lost or tuple
     "cat": "a small animal"
}
print(dictionary)"""


#(Q2) : You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed for all the students ?
#       "python","C++","java","python","javascript","java","python","java","C++","C"
# Done alone

"""subjects={"python","C++","java","python","javascript","java","python","java","C++","C"}
a=len(subjects)
print("Number of classrooms required-> ",a)"""


#(Q3) : Write a program to enter marks of three subjects from the user and store them in a dictionary . Start with an emoty dictionary and add .
# Done alone

"""print("Welcome to student record dictionary")
user_result={}
a=float(input("Enter your Physics marks: "))
b=float(input("Enter your Maths marks: "))
c=float(input("Enter your Chemistry marks: "))
user_result.update({"Physics": a})
user_result["Maths:"]= b
user_result.update({"Chemistry": c})
print("Student's marks record->",user_result)"""


# (Q3) : figure out a way to store 9 & 0.9 as seperate values in the set. (You can take help of built-in data types).
# Done with help ( python treats int=9 and ; float=9.0 as same due t same hash)

# method-1
"""values1={9,"9.0"}                         # stored as a string , or values1={"9",9.0}
print(values1)

# method-2
values2={9,(9.0,)}                        # stored as a tuple
print(values2)

# method-3
values3={
    ("float",9.0),                         # also stored as tuples
    ("intiger",9)
}
print(values3)"""


                                    # END