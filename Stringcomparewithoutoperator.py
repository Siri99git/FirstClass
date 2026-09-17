
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) != len(str2):
    print("Strings are not equal")
else:
    same = True

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            same = False
            break

    if same:
        print("Strings are equal")
    else:
        print("Strings are not equal")