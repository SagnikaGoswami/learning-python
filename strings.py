# Strings take a little extra space on memory, since string saves the unicode for every character 


a = "A"
print(ord(a)) # unicode of "A" which is, 65

b = 65
print(chr(b)) # character from the Unicode 65  which is, "A"


# Indexing
str1 = "Hello Coder"
print(str1[0]) # H
print(str1[-1]) # last character which is, r
print(str1[-2]) # e


# String Slicing [start : stop : steps]
str2 = "Python Programming"
print(str2[0 : 6 : 1]) # Python
print(str2[-11 : : 1]) # Programming
print(str2[-11 : : ]) # Programming
print(str2[7 : : ]) # Programming
print(str2[ : : ]) # Python Programming
# step = 1: means forward
# step = -1: means backward / reverse order
