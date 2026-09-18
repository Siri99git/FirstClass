#Data types in python


#integer

intvariable=10
print(intvariable)

#float

floatvariable=10.5
print(floatvariable)

#string

stringvariable="Hello"
print(stringvariable)

#boolean

booleanvariable=True
print(booleanvariable)

#set

setvariable={10,20,30,10,20}
print(setvariable)

#list

listvariable=[10,20,30,10,20]
print(listvariable)

#tuple

tuplevariable=(10,20,30,10,20)
print(tuplevariable)

#dictionary

dictvariable={"name":"John","age":30,"city":"New York"}
print(dictvariable)


import math


testingmath=math.sqrt(16)
print("sqrt", testingmath)

testingmath2=math.pow(2,3)
print("pow", testingmath2)

testingmath3=math.factorial(5)
print("factorial", testingmath3)

testingmath4=math.gcd(12,18)
print("gcd", testingmath4) 

testingmath5=math.lcm(12,18)
print("lcm", testingmath5) 

testingmath6=math.ceil(4.2)
print("ceil", testingmath6)

testingmath7=math.floor(4.8)
print("floor", testingmath7) 

testingmath8=math.fabs(-5)
print("fabs", testingmath8) 

testingmath9=math.fmod(10,3)
print("fmod", testingmath9)

#getdecimal points

decimalnumber=10.123456789
print("Decimal number:", decimalnumber)

#get only 2 decimal points
print("Decimal number with 2 decimal points: {:.2f}".format(decimalnumber))

#decimal module

from decimal import Decimal

decimalnum = Decimal("3.141592653589793238462643383279502884197")

print("Decimal number: ", decimalnum)

#String comparison

Stringforcomparison1="Hello"
Stringforcomparison2="hello"    

print("String comparison ==:", Stringforcomparison1 == Stringforcomparison2)

print("String comparison !=:", Stringforcomparison1 != Stringforcomparison2)

print("String comparison >:", Stringforcomparison1 > Stringforcomparison2)

print("String comparison <:", Stringforcomparison1 < Stringforcomparison2)

print("String comparison >=:", Stringforcomparison1 >= Stringforcomparison2)

print("String comparison <=:", Stringforcomparison1 <= Stringforcomparison2)

print("String comparison is:", Stringforcomparison1 is Stringforcomparison2)

print("String comparison is not:", Stringforcomparison1 is not Stringforcomparison2)

print("String comparison: in", Stringforcomparison1 in Stringforcomparison2)

#isspace() method

setvariable1="   "
setvariable2="Hel lo"
print("isspace() method:  ", setvariable1.isspace())
print("isspace() method: Hel lo", setvariable2.isspace())

#count() method

setvariableforcount="Hello World"
print("count() method: ", setvariableforcount.count("o"))

#substring() method

setvariableforsubstring="Hello World"
print("substring() method: ", setvariableforsubstring[0:5])

#stringcharactercount() method

stringforcharactercount="Hello World"
print("stringcharactercount() method: ", len(stringforcharactercount))

print("stringcharactercount() method: ", len(stringforcharactercount.split(" ")))
print("stringcharactercount() method: ", len(stringforcharactercount.split("o")))

print("Last character: ", stringforcharactercount[-1]) #last character


#any

anyvariable="Testing any data type"
anyvariable=10
print(type(anyvariable))
anyvariable={1,2,3,4}
print(anyvariable)
print(type(anyvariable))

anyvariable=None
print(type(anyvariable))


#and and or operators

andvariable1=True
andvariable2=False

if andvariable1 and andvariable2:
    print("Both are True")
else:
    print("One of them is False")   

if andvariable1 or andvariable2:
    print("One of them is True")    
else:           
    print("Both are False")

