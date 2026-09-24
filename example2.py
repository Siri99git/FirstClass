rows=5
for i in range(1, rows + 1):
    print('' * (rows-i)+ '*' * (2 * i - 1))


    a=1
    while(a<10):
       if a==5:
           a=a+1
           continue
       print("Hi" + str(a))
       a=a+1