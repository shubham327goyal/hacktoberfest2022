# height = input()
# python take input in string format only

# for x in range(0,10,1): # start , stop , step
"""
loop = True
while loop:
    name = input("insert something")
    if name == 'stop':
        loop = False
        break
"""


"""
fruits = ['apples' , 'pear' , 3]  # this is a list
fruits.append('strawberry')  #last me add hogya h
fruits[2] = 'blueberry'
print(fruits[2])
"""

"""
position = (2 ,3)
color = (255,255,255)  #this is a tuple

print(type(color))
"""

"""
fruits = ["apples", "pears", "strawberry"]
for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')
"""

"""
# strip len lower upper split
text = input('input something')

print(text.strip()) #strip remove white space aage piche vale
print(len(text))    #length of this string spaces are counted as length
print(text.lower())
print(text.upper())
print(text.split('.'))  #gets a list of all the values which are seperated by dots like a delimeter

"""

"""
#slice opreator

fruits = ['apples', "pear", 'strawberry']
text = 'hello i like python'

# start stop step
print(text[3:14:2])
fruits[3:3] = 'b'
print(fruits[1:])
"""



"""
def addTwo(x):
    return x+10

def subtractTwo(x):
    return x-10

print(addTwo(20))
print(subtractTwo(50))
"""



"""
# reading from a text file
file = open('file.txt', 'r')
f = file.readlines()
new_list = []
for lines in f:
    if lines[-1] == '\n':
        #new_list.append(lines[:-1])
        new_list.append(lines.strip())
        # strip function basically strip down the white sapces
    else:
        new_list.append(lines)
print(new_list)
file.close()
# r is basically here for stating that we are reading from the file
# w is for writing to the file
# a is for appending to the file
# r+ is for reading and writing to the file
# w+ is for reading and writing to the file
# a+ is for reading and writing to the file
"""



"""
file = open('file.txt', 'w')
file.write('hello world\n')
file.write("second line")
file.close()
# this will erase everything previously written in the file
"""

# .find() and .count() methods
"""
basically find will tell the first occurance of the element in the string 
and count will tell the number of occurances of the element in the string
and if the element is not present then find will return -1
"""


"""
# modular programming
# importing a module
import math
import myModule
print(myModule.myFun(10))
# we created a basic module out here and used it 
"""


"""
# optional parameter in function python
def function(x , y = 10):
    return x+y

print(function(10 , 4))
# here we used the optional parameter
# if we dont pass the optional parameter then it will take the default value
# if we pass the optional parameter then it will take the value of the optional parameter
# and optional parameter is always the last parameter in the function
# there can be more than one optional parameter
"""


"""
# we used this program to illustrate the use of try and except
# here we take input and check if it contain only numbeer or not
text = input("username: ")
try:
    number = int(text)
    print(number)
except:
    print("not a number")
"""


# gloabal and local variables in python
# here we use global keyword to use the variable defined outside the function


"""

# map function in python
li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x



newlist = []
for i in li:
    newlist.append(func(i))
print(newlist)

# we can replace above 4 lines to 1 line using map function
# map function takes a function as an argument and applies it to every element in the list
# and returns a list

print(list(map(func, li)))
# illustration of using map function

print([func(i) for i in li if i%2 == 0])
# this is also a cool method called list comprehension

"""

"""
# filter function

def add4(x):
    return x+4

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

# b = list(filter(isOdd, a))

c = list(map(add4, filter(isOdd, a)))
print(c)
# filter function returns a list of elements which satisfy the condition

"""


"""
# lambda function in python
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 65

func3 = lambda x: x+5
func4 = lambda x, y = 10: x+y

# lambda function is used to create a function without a name
# lambda function is one line function
print(func3(4))
print(func4(4))
print(func(4))

a = [1,2,3,4,5,6,7,8,9,10]
newlist = list(map(lambda x: x+5, a))
print(newlist)
"""



# collections
# collections is a module in python which contains many useful functions
# for example, we can use the Counter function to count the number of times a word appears in a text
# here we will see the use of counter function

#containers
#list
#tuple - immutable
#set - unordered and unindexed
#dict - unordered and indexed

#types
# counter
# deque
# namedtuple()
# ordereddict
# defaultdict


import collections
from collections import Counter
"""
c = Counter('shubham')
print(c)
m = Counter(['a', 'c', 'b', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(c)
c = Counter({'a':1, 'b':2, 'c':3})
print(c)
c = Counter(a=1, b=2, c=3)
print(c)
print(c['c'])
print(c['d'])
d = {'a':1, 'b':2, 'c':3}
print(type(d))
# print(d['r'])
# if its not there then it will return 0
# but in case of dictionary it will return error
# output looks like dictionary but it`s a bit different
c = Counter(cats = 4, dogs = 6)
print(list(c.elements()))
print(m.most_common(4))
"""


"""
c = Counter(a = 4, b = 2, c = 0, d = -2)
d = ['a', 'b', 'c', 'b']
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)

c = Counter(a = 4, b = 2, c = 0, d = -2)
d = Counter(['a', 'b', 'c', 'b'])

print(c+d)
print(c-d)
print(c & d)
print(c | d)
"""