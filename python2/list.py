"""fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)"""
# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)
"""
my_set = {"red", "green", "blue" }
print(my_set)
my_set.add("yellow")
print(my_set)
my_set.discard("green")
print(my_set)
print(len(my_set))"""
# a = {'name' : 'John', 'age' : '20'}
# b = {'name' : 'May', 'age' : '23'}
# customers = {'c1' : a, 'c2' : b}
# print(customers)
student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value) 