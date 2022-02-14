from random import shuffle
import array as arr
import random
import pickle


# square the number from 1:5 - generator function
# value = (x * x for x in range(1, 5))
# print(next(value))
# print(next(value))

def square_value(val):
    print('am inside the square value function')
    for each_val in range(val):
        print("yeah am inside the generator")
        yield each_val * each_val
        print("Hello")


gen = square_value(10)
while True:
    try:
        print("Received on next():", next(gen))
    except StopIteration:
        break

# Fibonacci generator - Corey Schafer
# Dict iteration
# Practice oops program over and over - self means instance of class;also practice using super
# list comprehension
# Python related ques - ready to ask your interviewer
# Diff between python 2 and 3
# Communicate with Databases - sqlalchemy
# Unit testing
# Basics of other technologies - github, basic sql code

# Ternary Operator
a = 10
b = 11
print("a > b") if a > b else print("b is greater than a")

list1 = ['hi', 10, 10.23, "bye"]
with open("./newfile.txt", "wb") as fHnd:
    pickle.dump(list1, fHnd)

with open("./newfile.txt", "rb") as fHnd:
    result = pickle.load(fHnd)

print(result)

input_array = arr.array('i', [10, 14, 54])
rev_arr = input_array[::-1]
print("Reverse array:", rev_arr)

mul_val = lambda a, b: a * b
print(mul_val(5, 5))

list1 = ["The", "name", "of", "an", "instrument", "is", "Violin"]
shuffle(list1)
print(list1)

input_value = random.randrange(1, 10, 2)
print(input_value)

# for element in range(10):
#   print('element:{element}')
