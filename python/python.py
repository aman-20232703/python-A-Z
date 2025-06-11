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
