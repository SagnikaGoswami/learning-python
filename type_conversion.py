# EXPLICIT Type Conversion

# Integer to String
a = 12
print(type(a)) # int

a = str(a)
print(type(a)) # str


# String to Integer
b = "12"
print(b)
print(type(b)) # str

b = int(b)
print(b)
print(type(b)) # int


# Integer to Boolean
c = 12
print(bool(c)) # True

d = 0
print(bool(d)) # False

# falsy values (7): False, 0, 0.0, "", [], (), {}



# IMPLICIT Type Conversion
print(12/3) # 4.0, converted to float