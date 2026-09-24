#fix the code


a=1
while(a<10):
       if a==5:
           a=a+1
           continue
       print("Hi" + str(a))
       a=a+1


# find the prime numbers between 1 and 100
for num in range(2, 11):
    for i in range(2, num):
        print("Checking if " + str(num) + " is divisible by " + str(i))
        if num % i == 0:
            break
    else:
        print(num)

#print * in a triangle pattern 
for i in range(1, 6):
    for j in range(i):
        print( "*", end="")
    print()

#print * in an inverted triangle pattern
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#print * in a triangle pattern
                                                    #              * 
                                                    #             ***
                                                    #            *****
                                                    #           *******  
rows = 5
for i in range(1, rows ):    # i = 1,2,3,4
    print(' ' * (rows - i) + '*' * (2 * i - 1))
       