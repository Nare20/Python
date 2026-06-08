# class Calculator:
#   def add(self, a, b):
    # return a + b
#   def sub(self,a,b):
    # return a * b
#   def mul(self,a,b):
    # return a - b
    

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.sub(4, 5))
# print(calc.mul(8,4))
# class Pen:
    # def use(self):
        # return "Writing"

# class Eraser:
    # def use(self):
        # return "Erasing"

# def perform_task(tool):
    # print(tool.use())

# perform_task(Pen())
# perform_task(Eraser())
# class Calculator:
    # def multiply(self,a=7, b=8,*args):
        # result = a*b
        # for num in args:
            # result *=num
        # return result
    
# calc = Calculator()

# print(calc.multiply())
# print(calc.multiply(4))

# print(calc.multiply(2,3))
# print(calc.multiply(2,5,6))

class Animal:
    def sound(self):
        return "some sound"
    def eat(self):
        return "Eating"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    def eat(self):
        pass
class Cat(Animal):
    def sound(self):
        return "Meow"
    
animals = [Dog(), Animal(),Cat()]
for animal in animals:
    print(animal.sound())
    print(animal.eat())
