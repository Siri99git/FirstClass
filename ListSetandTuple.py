
'''
Feature	     List []	    Set {}	           Tuple ()
Ordered	      Yes	    No guaranteed order	    Yes
Duplicates	Allowed	        Not allowed	        Allowed
Mutable     	Yes	        Yes             	No
Indexing	    Yes	        No	                Yes
Main use	Shopping cart	Unique customers	Fixed product details
'''


# 1. LIST - Shopping cart
cart = ["Laptop", "Mouse", "Keyboard", "Mouse"]

print("Shopping Cart:", cart)

# Add a new item
cart.append("Headphones")

# Remove an item
cart.remove("Keyboard")

print("Updated Cart:", cart)


# 2. SET - Unique categories
categories = {"Electronics", "Clothing", "Electronics", "Books"}

print("Categories:", categories)

# Add new category
categories.add("Groceries")

# Remove category
categories.discard("Books")

print("Updated Categories:", categories)


# 3. TUPLE - Fixed product details
product = (101, "Laptop", 75000)

print("Product ID:", product[0])
print("Product Name:", product[1])
print("Product Price:", product[2])



# LIST: Students registered for courses
students = ["Ravi", "Sita", "John", "Ravi"]

# SET: Unique student names
unique_students = set(students)

# TUPLE: Fixed course information
course = (101, "Python Programming", 3)

print("All Registrations:", students)
print("Unique Students:", unique_students)
print("Course Details:", course)

# Add a student
students.append("Priya")

# Add unique student
unique_students.add("Priya")

# Access course details
print("Course ID:", course[0])
print("Course Name:", course[1])
print("Duration:", course[2], "months")

print("Total Registrations:", len(students))
print("Unique Student Count:", len(unique_students))

'''
Online shopping application
Scenario:
- List: Store items added to a shopping cart.
- Set: Store unique product categories.
- Tuple: Store fixed product information such as product ID, name, and price.
'''

# 1. LIST - Shopping cart
cart = ["Laptop", "Mouse", "Keyboard", "Mouse"]

print("Shopping Cart:", cart)

# Add a new item
cart.append("Headphones")

# Remove an item
cart.remove("Keyboard")

print("Updated Cart:", cart)


# 2. SET - Unique categories
categories = {"Electronics", "Clothing", "Electronics", "Books"}

print("Categories:", categories)

# Add new category
categories.add("Groceries")

# Remove category
categories.discard("Books")

print("Updated Categories:", categories)


# 3. TUPLE - Fixed product details
product = (101, "Laptop", 75000)

print("Product ID:", product[0])
print("Product Name:", product[1])
print("Product Price:", product[2])


print(product)


'''
Application	            List	        Set                     	Tuple
Banking	            Transactions	Unique transaction types	Account details
Netflix	            Watch history	Unique genres	            Movie details
HR	                Login records	Unique employees	        Employee details
Food delivery	      Ordered items	Unique food items	        Restaurant details
E-commerce	        Shopping cart	Unique product IDs	        Product record
Flight booking	Passenger bookings	Unique destinations	        Flight details
'''


'''
Stores the login records using a list.
Finds the unique employees using a set.
Stores company information using a tuple.
Prints the total number of logins.
Prints the number of unique employees.
Prints how many times each employee logged in.

'''


logins = ["John", "Mary", "John", "David", "Mary", "Alex"]

unique_employees = set(logins)

company = (1001, "ABC Technologies", "Dallas")

print("Company:", company)
print("Total Logins:", len(logins))
print("Unique Employees:", len(unique_employees))

for employee in sorted(unique_employees):
    print(employee, ":", logins.count(employee))
