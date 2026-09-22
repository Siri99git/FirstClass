s = "hello world"
old = "hello"
new = "Python"

result = ""
i = 0

print("String  "+s[i:i + len(old)] )

while i < len(s):
    if s[i:i + len(old)] == old:
        result += new
        i += len(old)
        print("IF"+result)

    else:
        result += s[i]
        i += 1
        print("ELSE"+result)

        
print(result)


#replace string
stringforreplace="Hello World"
print("replace string: ", stringforreplace.replace("Hello", "Python"))