# 4 Check voting eligiblity

age = int(input("Enter your age: "))

if age >= 18:
    print("You are a valid voter")
elif age < 18 and age > 0:
    print("You are not eligible to vote")
else:
    print("Invalid age input")
