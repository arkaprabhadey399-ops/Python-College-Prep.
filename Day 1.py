print("======Welcome to the Grade calculation System")
name = input("Enter your name: ")
class_name = int(input("Enter your standard: "))
marks = int(input("Enter your marks: "))

print("\n--- Report Card ---")
print("Name:", name)
print("Class:", class_name)
print("Marks:", marks)

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
elif(0<=marks<40):
    grade = "Fail"
else:
    print("ERROR!\nPlease enter a valid marks between 100")

print("Your Grade:", grade)

print("\n--- Student Analysis ---")
a=marks + 5

if (marks>=95):
    if(marks==95):
        print("Next year, your target should be:", a)
    elif(marks==96):
        print("Next year, your target should be:", marks + 4)
    elif(marks==97):
        print("Next year, your target should be:", marks + 3)
    elif(marks==96):
        print("Next year, your target should be:", marks + 2)
    elif(marks==96):
        print("Next year, your target should be:", marks + 1)
    else:
        print("WOW !\n You have score perfectly.\nKeep it up")
else:
    print("Next year, your target should be:", a)

print("\nThank you for using the system 🚀")