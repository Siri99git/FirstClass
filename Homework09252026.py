#1. How can you create as python instead of single char

#2. Without using copy and mohan[:] symbol how to copy list.

#3. set methods what is update doing. there is no 4th position and trying to update value for 4th position.

#4. tuple t2=(1,) what will happen

#5. tuples 

#6. %s , %d means %.2f


from itertools import count


print(list("python"))

for char in "python":
     print(char, end="")

print("\n-----")

text = "python Java .net"

result = []
word = ""

for char in text:
    if char == " ":
        if word:
            result.append(word)
            word = ""
    else:
        word += char

if word:
    result.append(word)

print(result)

print("\n-----")

list1 = [10, 20, 30]

new_list = []

for x in list1:
    new_list.append(x)

print(new_list)

print("\n-----")

s = {10, 20, 30}

s.update([40, 50])

print(s)

print("\n-----")    

t2 = (1,)

print(type(t2))
print(t2)   
print("\n-----")

name = "Siri"

print("Name is %s" % name)
print("\n-----")

price = 10.56789
print(f"Price is {price:.2f}")
print("\n-----")    

age = 30

print("Age is %d" % age)