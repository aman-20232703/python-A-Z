""" # calculator

a = int(input("enter 1st number: ", ))
b = int(input("enter 2nd number: ", ))

print("required results:- ")

#for addition
adddition=a+b
print("1.adddition of",a,"and",b,"is",adddition)

#for subtraction
subtraction=a-b
print("2.subtraction of",a,"and",b,"is",subtraction)

#for multiplication
multiplication=a*b
print("3.multiplication of",a,"and",b,"is",multiplication)

#for division
division=a/b
print("4.division of",a,"and",b,"is",division)

print("thankyou :)")

"""

"""
# typcasting

string ="12"
number= 2

string_number=int(string)
add1=number+string_number
print("addition is:",add1)  # explicit typecasting
print("type of this variable",type(add1))

# add=string+number
# print("addition",add)

b=2.9
c=3
d=b+c
print("addition is:",d)  # implicit typecasting(python intrpreter automatically convert it according to requirement)
print("type of this variable",type(d))

"""

"""
# taking user input in python
a = input("enter number: ")
b = input("enter number: ")
print(a+b)             # it assume all the variable as string
print(int(a)+int(b))   # there we need to initialize datatype of our variable- "int"

"""

"""
# string
fruits="mango"
print(fruits[1:4])
print(fruits[:5])
print(fruits[0:-3])  # print(fruits[0:len(fruits)-3])
print(fruits[-3:-1])

na="harry"
print(na[-4:-2])

"""

"""
#string method
a ="aMAn kUmAr is gooD bOy00"
print(a.lower())
print(a.upper())
print(a.rstrip("!"))
print(a.replace("aMAn","aman"))
print(a.split(" "))
print(a.capitalize()) #
print(len(a))
print(len(a.center(8)))
print(a.count("aMAn"))
print(a.endswith("kUmAr"))
print(a.endswith("mA",7,9))
print(a.startswith("aMAn"))
print(a.find("is")) #return - sign also
print(a.index("A"))  # sure to return , not return - sign

d="ramanujan college"
print(d.isalnum())
print(d.isalpha())
print(d.islower())
print(d.isupper())

b ="aMAn kUmAr is GooD bOy00"
print(b.isprintable())
print(b.isspace())   # " "=whitespace
print(b.istitle())
print(a.title())

c="aman kumar"
print(c.swapcase())

"""

# conditional statements
"""#else-if
a=int(input("enter your age: "))

if(a>18):
    print("ready")
else:
    print("not ready")

#elif
a=int(input("enter your age: "))
if(a>18):
    print("yes")
elif(a<18):
    print("no")
else:
    print("none")
print("thankyou")
    
#nested-if
a=int(input("enter your age: "))

if(a<18):
    print("no")
elif(a>18):
    if(a==20):
        print("yes")
    elif(a<30):
        print("none")
    else:
        print("ok")
print("thankyou")


import time
tm=time.strftime("%H:%M:%S")
print(tm)
tm=time.strftime("%H")
print(tm)
tm=time.strftime("%M")
print(tm)
tm=time.strftime("%S")
print(tm)

a=int(input("select standard time zone: "))
if(a<11):
    print("good morning")
elif(a>11 and a<14 ):
    print("good afternoon")
else:
    print("good evening")
    

x=int(input())

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)
