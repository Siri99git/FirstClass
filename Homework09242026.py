

data = [10, "apple", 5, "banana", 2.5, 20]
numbers = []
strings = []

for item in data:
    if isinstance(item, (int, float)):
        numbers.append(item)
    elif isinstance(item, str):
        strings.append(item)

numbers.sort()
strings.sort()

result = numbers + strings

print(result)


# The code above separates numbers and strings from a mixed list, sorts them individually, and then combines them back together.

# This approach ensures that numbers and strings are handled separately, allowing for proper sorting and combination.
# The code demonstrates the use of type checking and list comprehensions for organizing and sorting data.
# It also highlights the importance of handling different data types separately to achieve the desired result.

# Example usage:
# data = [10, "apple", 5, "banana", 2.5, 20]
# The expected output is [2.5, 5, 10, 20, "apple", "banana"]

# input any numbers list print only the prime numbers from the list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
for n in numbers:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)

# input any number list print only even numbers from the list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
for n in numbers:
    if n % 2 == 0:
        print(n)        
        
# input any number list print only odd numbers from the list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
for n in numbers:
    if n % 2 != 0:
        print(n)

