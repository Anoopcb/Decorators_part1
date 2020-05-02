## you have to have a complete understanding of functions
# first class function
##closers

def square(a):
    return a**2
s = square
print(s(7))
print(square(7))
print(s.__name__)
print(square.__name__)

print(s)
print(square)



## passing function as an agrument
# map function

l = [1, 2, 3, 4]


print(list(map(s, l)))

def my_map(func, l):
    new_list = []
    for item in l:

     new_list.append(func(item))
    return new_list

print(my_map(square, l))

print(my_map(lambda a: a**3, l))
## by list comprehension

def my_map2(func, l):
    return [func(item) for item in l]



print(my_map(square, l))


## function returning function

def outer_func():
    def inter_func():
        print("inside inner func")
    return inter_func


var = outer_func()

var()


def outer_func2(msg):
    def inter_func2():
        print(f"message is {msg}")
    return inter_func2


var = outer_func2("Hi there!")

var()


##closers

##function returning fucntion

def to_power(x):
    def calc_power(m):
        return m**x
    return calc_power


cube = to_power(3)
print(cube(5))

square1 = to_power(2)
print(square1(2))

## Decorators intro:- enhance the functionality of other functions


# this is awesome function

def decorator_func(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function

def func1():

    print("this is function one")

def func2():
    print("This is fucntion two")


var = decorator_func(func1)
var()


var = decorator_func(func2)
var()

## @use for decorators

@decorator_func


def func1():

    print("this is function one")
func1()





