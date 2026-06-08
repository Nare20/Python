"""def display_message(name):
    print("I am learning about function in Python, ", name, "!")
display_message("Nare")
def describe_pet(animal_type, pet_name):
   
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
descripe_pet()
def getformat_name(first_name, last_name):
    full_name = "hello " + first_name + " " +last_name
    return full_name.title()
musician = getformat_name("jimi", "helen")
print(musician)
def getformat_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = first_name + " " +last_name + " " + middle_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
musician = getformat_name( "nare" , "grigoryan ", " ka ")
print(musician)
musician = getformat_name( "nare" , "grigoryan")
print(musician)
def add_num(*a , b):
    if a % 2 == 0:
        return a + b
    elif (a - b) < 0:
        return "c"

    else:
        return a-b
number = add_num(15,16,8)
print(number)
def sum_number(*args):
    s = 0
    p = 1
    for x in args:
        s+= x
        p*= x
    return s , p
print(sum_number(10,15,6))
print(sum_number(2,3))

def my_list(first_list):
    empty_list = []
    for x in first_list:
        if x % 2 == 0:
            empty_list.append(x)
    return empty_list
print(my_list([2,6,11,15,18]))"""
# def arthimetic(num1, num2):
    # add = num1 + num2
    # div = num1 / num2
    # sub =  num1 - num2
    # mul = num1 * num2
    # return add, div, sub, mul
# a,b,c,d = arthimetic(10,5)
# print("sub = ",c)
# print("mul = ",d)
# print("div = ",b)
# print("add = ",a)
# gobal_lang = 'DataScience'
# def var_scope_test():
    # local_lang = 'Python'
    # print(local_lang)
    # printglobal_lang)
# var_scope_test()
# print(local_lang)
# global_lang = 888
# def function1():
    # print("The vale of ", global_lang)
# def function2():
#    global global_lang 
#    global_lang = 44
#    print("I change " , global_lang)
 
# function1()
# function2()  
# print(global_lang)
# def greet_user(name):
    # def greet():
        # return f"Hello, {name}!"

    # return greet()

# print(greet_user("Alice"))d\
# def calculate_area(shape,dimension):
    # def circle_area(radius):
        # return 3.1 * radius * radius
    # def squere_area(side):
        # return side*3
    

    # if shape == 'circle':
        # return circle_area(dimension)
    # elif shape == 'square':
        # return  squere_area(dimension)


# print(calculate_area("circle",5))
# print(calculate_area("square",6))
# def multiplier(factor):
    # def multiply_by(n):
        # return n * factor

    # return multiply_by
# multiply_by_3 = multiplier(3)
# print(multiply_by_3(10))  

# multiply_by_5 = multiplier(5)
# print(multiply_by_5(10)) 
# def power(exponent):
    # def raise_to_power(base):
        # return base ** exponent
    # return raise_to_power
# square = power(2)
# cube = power(3)

# print(square(4))
# print(cube(9))
# def make_adder(x):
    # def make_adder_by(base):
        # return base ** x
    # return make_adder_by
# deff = make_adder(3)
# serr = make_adder(2)
# print(deff(7))
# print(serr(8))
# def my_decorator(func):
    # def wrapper():
        # print("Something is happening before the function is called.")
        # func()
        # print("Something is happening after the function is called.")

    # return wrapper

# @my_decorator
# def say_hello():
    # print("Hello!")

# say_hello()
# def example(a,b):
    # if a * b <= 1000:
        # return a * b
    # else:
        # return a + b
# a =int(input(" a = "))
# b =int( input(" b = "))
# print(example(a , b))
# previus = 0
# for current in range(10):
    # total = current + previus
    # print(current, previus)
    # previus = current
    # print(current, previus)
# my_list = []
# for i in range(2000,3300):
    # if i%7 == 0 and i % 5 != 0:
        # my_list.append(str(i))
# print(my_list)
# n = int(input("n = "))
# d = dict()
# for i in range(1,n+1):
    # d[i] = i*i
# print(d)