"""
# calculator

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

"""
# conditional statements

#else-if
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
"""


"""
# for loops(iterate over a sequence of iterable or objects)
k="aman kumar"
for i in k:
    print(i)
    
for i in range(5):
    print(i)
    
for i in range(3,8):
    print(i)
    
for i in range (1,100,7):
    print(i)
    
list=["aman","putu","suraj","vikash"]
for i in list:
    print(i)
"""

"""
# while loops(print only if condition satisfied)
# count=0
# while(count<=5):
#     print(count)
#     count+=1
# else:
#     print("finish")
    
t=5
while(t>=0):
    print(t)
    t-=1
"""

"""
# break statement enable a programme to skip over a part of code, it also terminate the loop.
for i in range(12):
    if(i==10):
        break
    print("5*",i+1,"=",5*(i+1))
print("outside of loop")

# continue terminate the iteration and jump into the next iteration
for i in range(12):
    if(i==10):
        print("skip it")
        continue
    print("5*",i+1,"=",5*(i+1))
"""

"""
# function is a lock of code that perform specific task whether it is called, is help reduce same line code uses at diffrent palce by calling function 
def greatervalue(a,b):

    if(b>a):
        print("b greater")
    else:
        print("not grater")
    # a=4
    # b=6
greatervalue(3,5)
"""


"""
# argumnets(default,keyword,variable,required)
#default
def sum(a=4,b=5):
    print("sum is: ",a+b)
sum() # by default from above function
"""

"""
#keyword
def sum(a=3,b=5):
    print("sum is: ",a+b)
sum(b=3,a=22) #position not matter

#required
def sum(a,b=5):
    print("sum is: ",a+b)
sum(3)  #required a value to run the function

#variable
def avg(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("avg is: ",sum/len(numbers))
avg(1,2,3,4,5,6,7,8,9,10) #variables as a tuple

#return
def sum(a,b):
    return a+b
c=sum(2,5)   # c value store result of return
print("sum is:",c)
"""

"""
#list(seperated by comaas and square barcket, store multiple data in same variable, mutable, can have diffrent data types, denoted by [...])
marks=[22,4,34,56,23,67]
print(marks)
print(type(marks))
print(marks[4])
print(marks[-3])  #print(marks[len(marks)-3])=3 index  ,print(marks[6-3]),print(marks[2])

if 4 in marks:
    print("yes")
else:
    print("no")
    
if "ma" in "aman":
    print("yes")
else:
    print("no")
    
print(marks[:])
print(marks[1:])
print(marks[1:6:2])

#list comprehension
list=[i for i in range(20) if i%2==0]
print(list)
"""

"""
#methods in list
l=[2,3,4,5,1,6]
# l.append(55)
# l.insert(4,100)
# l.extend([33,56,48])

# print(l.sort() )#ascending order
# print(l.sort(reverse=True) )#descending order
# print(l.reverse())

print(l.index(5))
print(l.count(5))
print(l.copy())

k=[22,88,34,78]
m=l+k
print(m)
print(l)
"""

"""
#tuples(similar to list but only difference is that it is immutable, denoted by(....))
tup=(1,2,3,4,5,6)
print(tup,type(tup))
print(len(tup))
print(tup[4])
print(tup[:5])
print(tup[len(tup)-4:5])

if 4 in tup:
    print("yes")
else:
    print("no")
    
tup=(i for i in range(10) if i%2!=0)
print(tup)
"""

"""
# methods in tuple
n=("aman","raj","aditya","sahil")
p=list(n)  #if we try to change tuple then first convert it into list
print(p)
p.append("vikash")
print(p)
p.pop(2)
print(p)
n=tuple(p)   # after doing changing in tuples convert again it into list
print(n)

#methods in tuple
n=(2,3,6,7,2,8,3,9)
print(n.count(2))
print(n.index(8))
print(n.index(7,3,6))
print(len(n))
"""

"""
import time
hour=int(input("enter your timing-: "))
# a=int(input("select standard time zone: "))
if(hour>0 and hour<12):
    print("good morning")
elif(hour>11 and hour<17 ):
    print("good afternoon")
elif(hour>17 and hour<24):
    print("good evening")
"""

"""
#f-string
letter="my name is {1} and i am from {0}"   #using indexing
name="aman kumar"
country="India"
print(letter.format(country,name))
print(f"my name is {name} iam from {country}") # using f-string

txt="for only {price:.2f} dollars!"  #using 2 decimal places
print(txt.format(price=49.99999))
price=49.99999
print(f"for only {price:.2f} dollars!")

#doc-string(string litrals that appear right after the defination of a function,method,class or method) & PEP-8
def square(n):
    '''take a nunmber n, return the square of n'''  # always come below or above function,method,class
    print(n**2)
square(5)
print(square.__doc__)  # accessing docstring using this doc attribute
"""

"""
# PEP-8(python enhancement proposal) is type of guidelines provided in the python
The Zen of Python, by Tim Peters:-
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""

"""
# PEP-8(python enhancement proposal) is type of guidelines provided in the python
The Zen of Python, by Tim Peters:-
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


"""
# set is a collection of well defined object, it store unordered, multiple and unique items in {} bracket, unchangable, contain different datatypes,
s={1,2,3,4,2,5,4,7,8,9,5}
print(s)
print(type(s))

a={}
print(type(a))  #it gives empty dict...
b=set()
print(type(b))  # it gives empty set

q={"Aman",3,77,"Kumar","@",0,12}
for i in q:
    print(i)   # unordered
    
#methods in set
s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)

states={"bihar","up","jharkhand","mp","rajsthan","haryana"}
states2={"maharastra","karnataka","tamilnadu","bihar","mp"}
# states3=states.union(states2)
# print(states,states2,states3)

# states3=(states.intersection(states2))
# states.intersection_update(states2)
# print(states)
"""

"""
print(states.symmetric_difference(states2))  # not common
print(states.symmetric_difference_update(states2))
print(states.difference(states2)) # delete common
print(states.isdisjoint(states2))  #intersection zero
print(states.issuperset(states2))  # all the elements of states2 lie within states
print(states2.issubset(states))  #vice-versa
# states.remove("bihar")
states.discard("bihar")  # same work as remove but it does not throw error
print(states)
print(states2.pop())  # delete random value anywhere from set
del states
print(states2) # it is not a method , it delete set entirly

z={1,2,3,4,6,7}
print(z.clear())
"""

"""
print(states.symmetric_difference(states2))  # not common
print(states.symmetric_difference_update(states2))
print(states.difference(states2)) # delete common
print(states.isdisjoint(states2))  #intersection zero
print(states.issuperset(states2))  # all the elements of states2 lie within states
print(states2.issubset(states))  #vice-versa
# states.remove("bihar")
states.discard("bihar")  # same work as remove but it does not throw error
print(states)
print(states2.pop())  # delete random value anywhere from set
del states
print(states2) # it is not a method , it delete set entirly

z={1,2,3,4,6,7}
print(z.clear())
"""

"""
# dictionaries(store key value items in key : value pairs tha are seperated by , and denoted {}, unordered)
dict={
    2703:"aman",
    2708:"brijesh",
    2731:"rupesh",
    2741:"suraj",
    2745:"vikash",
    2778:"sahil"
}
print(dict)
"""

"""
info={"name":"aman", "age":20, "course":"B.voc"}
print(info)
print(info["name"])
# print(info["name2"]) #if not exist throw error
print(info.get("name2")) #if not exist print none
print(info.get("name")) #if exist print
print(info["age"])

print(info.keys())  #printing keys
for key in info.keys(): #1st method for printing values
    print(info[key])
print(info.values()) #2nd method for printing values

print(info.items())  #accessing 'key : value' of dict....
print(dict.items())

#methods in dict...
ep1={2703:"aman",2708:"brijesh",2731:"rupesh",2741:"suraj",2745:"vikash",2778:"sahil"}
ep2={2749:"ashutosh",2729:"ritik"}

ep1.update(ep2)
# ep1.clear()
# ep1.pop(2741)
# del ep1[2745]
ep1.popitem()  # delete last
print(ep1)
"""

"""
#for-else loop
for i in range(9):
    print(i)
else:                # loop khtm hogya so execute else
    print("sorry no i")

for i in range(9):  # loop break ho gya hai so not execute else
    print(i)
    if i==4:
        break
else:
    print("sorry no i")
"""

"""
# excepion handling[try:except](process of responding to unitended and unexpected events when a computer programme runs,it help to mainatain flow of code)
# from logging import exception
n=input("enter value: ")
print(f"multiplication table of {n} is: ")
try:
    for i in range (1,11):
        print(f"{int(n)}X{i}={int(n)}*{i}")
except:
    print("invalid input:")
    
print("imp")
print("last...")

try:
    p=int(input("enter value number: "))
    a=[3,8]
    print(a[p])
except ValueError:
    print("number is not integer.")
except IndexError:
    print("index number error")
"""

"""
#finally clause(it is always excecuted in exception handeling so so it is generally used for doing conclusion task like closing the resources and closing the databases connection of may be ending teh programme)
try:
    a=[1,4,7,3,9,5]
    l=int(input("enter the index: "))
    print(a[l])
except:
    print("some error Occured")
finally:
    print("i am always Excecuted")   # we can also print above statement without finally but it cannot use within function

def function():
    try:
        a=[1,4,7,3,9,5]
        l=int(input("enter the index: "))
        print(a[l])
        return 1
    except:
        print("some error Occured")
        return 0
    finally:
        print("i am always Excecuted")
x=function()
print(x)
"""

"""
#raise custom error(we can create our own error to check evry steps of code & debugging)
a=int(input("enter any value between 2 ana 9: "))
if(a<2 or a>9):
    raise ValueError("value not in range")
else:
    print("ohh! great,value in range")
"""
