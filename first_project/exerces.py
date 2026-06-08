# def my_function(num1, num2):
#     product = num1 * num2

#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2
# print(my_function(20,30))
# print(my_function(40,30))

# privous = 0
# for current in range(0,10):
#      sum_num = privous + current
#      print(
#         f"Current Number = {current} | "
#         f"Previous Number = {privous} | "
#         f"Sum = {sum_num}"
#     )
#      privous = current

# my_word = "pynative"   
# for i in range(len(my_word)):
#     if i % 2 == 0:
#         print(my_word[i])
    
# age = 12
# if age > 18:
#     massage = "eligbel"
# elif age == 20:
#     massage = "not eligble"
# else:
#     massage = "yes"
# print(massage)
# sucsessful = False
# for number in range(3):
#     print( "attempt", number )
    
#     if sucsessful:
#         print("sucssesful")
#         break
# else:
#     print("false")
# for x in range(5):
#     for y in range(3):
     
#         print(f"({x}, {y})")

# while True:
#     command = input(">")    
#     if command.lower() == "quit":
#         break
        
   
#     print("Echo" , command)
# count = 0
# for i in range(1,10):
#     if i % 2 == 0:
#         count += 1
#         print(i)
# print(f"(we have count numbers {count})")

# def multiply(x,*y):
#     total = 1
#     return x * y
# result = multiply(2,3,5,7,8,9)
# print(result)
# unit = "yes"
# area = 200
# def calc_area(lenght, whith):
#     area =  lenght * whith
#     return area
# my_area = calc_area(20,15)
# print(my_area, unit)
# print(area)
# def greet(name):
#     return "Hello " + name

# greeting = greet("Alice")
# greet("Bob")
# print(greeting)

# def add(a,b):
#     return a + b
 
# result = add(10,15)
# print(result)
# print(add(result, 20))

# def compute(a,b):
#     result =  a*b
#     if result > 10:
#         return result -3
#     return result + 4
# print(compute(4,2))
# print(compute(4,10))
# try:
#     num = float(input("say "))
#     num2 = int(input("say2 "))
#     bajanel = num / num2
#     print(bajanel)
# except:
#     print("invalid ")
import time
def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f"Task time: {end_time - start_time} secons")
        return enhanced_fn
@timer_dec   
def brew_tea():
    print("Brewing tea... ")
    time.sleep(2)
    print("tesa is ready!")

brew_tea()
