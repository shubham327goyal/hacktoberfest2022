# object oriented programming in python


"""
class dog(object):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        self.li = [1,3,4]

    def speak(self):
        print("hello i am", self.name, self.age)

    def talk(self):
        print("bark")

#example of inheritance

class cat(dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("meow")

hello = cat('shubham' , 22, 'black')
hello.speak()
hello.talk()

"""



"""
#overloading methods in pyhton
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x , self.y)

    def move(self, x , y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self , p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __eq__(self, other):
        return self.length() == other.length()

p1 = Point(1,2)
p2 = Point(3,4)
p3 = Point(5,6)
p4 = Point(7,8)
p5 = p1 + p2
p6 = p3 - p4
p7 = p1 * p2

print(p5, p6, p7)
print(p1 > p2)
print(p1 >= p2)
print(p1 < p2)
print(p1 <= p2)
print(p1 == p2)
"""

class _private:    # start with one underscore meaning that it is in private mode
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self,name):
        self.name = name
        self.private = _private(name)
    def _display(self):         # private method
        print("hello")
    def display(self):
        print("heo")

# in python there is nothing like private and public but we use only because other can understand
# anyone can acccess private one but its adviced not to use it