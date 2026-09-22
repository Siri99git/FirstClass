#Homework:
#1. One example with “not equal to” with condition
#2. what is static and dynamic with respect to datatypes
#3. Reverse string with different method( without using symbol)
#4. Why import should be at start
#5. 6 escape charecters with code


#1. One example with “not equal to” with condition

firstvalue = 10
secondvalue = 20

if firstvalue != secondvalue:
    print("The two values are not equal.")

#2. what is static and dynamic with respect to datatypes

x = 10
print(type(x))

x = "Hello"
print(type(x))

x = 10.5
print(type(x))

#3. Reverse string with different method( without using symbol)

name = "Sireesha"
reverse = ""

for ch in name:
    reverse = ch + reverse

print(reverse)

#4. Why import should be at start   The main reasons are readability, maintainability, and availability.

#5. 6 escape charecters with code

# 1. Newline
print("Hello\nWorld")

# 2. Tab
print("Name\tAge")

# 3. Backslash
print("C:\\Users\\Siri")

# 4. Single quote
print('It\'s Python')

# 5. Double quote
print("She said \"Hello\"")

# 6. Carriage return
print("Hello\rHapp")


