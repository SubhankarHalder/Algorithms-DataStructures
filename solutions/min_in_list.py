"""
Minimum Number in a list
"""
import random
import math

new_list = [random.randint(1, 19) for i in range(10)]

print("New List: ", new_list)
print("")

min = math.inf
for number in new_list:
    if number < min:
        min = number

print("Minimum Number: ", min)
print("")



