# Output

print("Hello, how are you?")

language = "Python"
print(language)

# formatted string
print(f"Hello, I am learning {language}!") # Hello, I am learning Python!


# Input
# input("Hello, enter a number: ") # this input is saved in any garbage memory

# input function always returns a string, so in case of numbers we need to perform type conversion 
num = int(input("Hello, enter any number: "))
print(f"User entered: {num}")
