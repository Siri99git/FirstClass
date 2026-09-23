#Type casting

x = "100"

y = int(x)

print(y)        # 100
print(type(y))  # <class 'int'>

age = 25

text = str(age)

print(text)
print(type(text))  # <class 'str'>

#else for loops

for i in range(5):
    print(i)
else:
    print("Loop completed")

#Else executes when for loop executes normally

#without membership operator string compare

text = "Hello Python"
sub = "Python"

found = False

for i in range(len(text) - len(sub) + 1):
    match = True

    for j in range(len(sub)):
        if text[i + j] != sub[j]:
            match = False
            break

    if match:
        found = True
        break

if found:
    print("Substring found")
else:
    print("Substring not found")

#with operator

text = "Hello Python"
sub = "Python"

if sub in text:
    print("Substring found")
else:
    print("Substring not found")