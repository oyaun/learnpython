"""
This document was prepared for just learning
by oyaun
"""

import os

strtest = "Hello World"
print (strtest[1])

a = 2
b = 5

print(b)
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")


x, y, z = "Orange", 'Banana', "Cherry"
print(x, y, z)


def my_func():

    global x
    x = "Oya"
    print(x)

my_func()

os.system("ping -c 3 google.com")

exit()
