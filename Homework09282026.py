numbers = [1, 2, 3, 4, 5]

squares = []

for x in numbers:
    squares.append(x * x)

print(squares)

print("\n-----")

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
print("\n-----")    

a = ["a", "b"]
b = [1, 2]

d = dict(zip(a, b))

print(d)
print("\n-----")    

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total = total + num

print(total)
   

