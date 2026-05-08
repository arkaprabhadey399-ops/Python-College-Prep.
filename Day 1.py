
name = "Sam"
class_name = "12"
marks = 99

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
else:
    grade = "Fail"

print("Grade:", grade)

print("\n--- Analysis ---")
print("Next year, your target should be:", marks + 5)

print("\nThank you for using the system 🚀")