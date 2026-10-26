# Arithmetic Operators
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Floor Division //
# Modulo %
# Exponential **

a = 5
b = 20
print(a + b)
print(b - a)
print(a * b)

c = b/a
print(c) # 4.0
print(type(c)) # float

d = b//a 
print(d) # 4
print(type(d)) # int

print(5**2) # 5^2 = 25
print(5**3) # 5^3 = 125

print(32%5) # remainder, 2

# Operator Precedence using BODMAS (Bracket Of Division Multiplication Addition Subtraction)
print(12 + 4 / 2) # 12 + 2.0 = 14.0



# Assignment Operators
x = 23

# Compound Assignment Operations
# we can re-assign values
y = 20
y = y + 20
y += 40
y += 60
print(y)



# Comparison Operators (always returns either True or False)
# >, <, >=, <=, ==, !=
w = 12.1
z = 12
print(w == z) # False
print(w != z) # True
print(w > z) # True
print(w < z) # False
print(45 <= 67) # True
print(23 >= 23) # True

# Strings are compared based on the ASCII values
print(ord("A")) # 65

print(chr(65)) # "A"

print(ord("B")) # 66

print("A" > "B") # False 
print("ABC" >= "AAC") # True

# print("A" > 34) # Error

print("A" > "34") # True
# Comparison between two strings is valid
# In the above statement, "A" is 65 and "3" is 51, so returns True



# Logical Operators (and, or, not)
print(123 > 100 and 34 == 34 and 45 < 90) # True
print(123 > 100 and 34 == 34 and 45 < 90 and 12 > 20) # False

print(12 != 12 or 23 == 45 or 67 == 56 or 10 > 5) # True

print(not 12 == 12) # False

