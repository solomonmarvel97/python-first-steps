"""
For shorts, a module is simply a python file
The python file can contain classes, functions and even variables

And the classes, functions or variables can be imported to other files
"""


from circle import area_of_a_circle
from rectangle import area_of_a_retangle

# called the area of a circle function
print(area_of_a_circle(10))

# called the area of a rectangle function
print(area_of_a_retangle(5, 5))



# example
from greeting import greeting, sayHi
print(greeting("Evening", "Marv"))
print(sayHi("Ella"))


# example
from functions.sayHello import sayHello
from functions.sayHi import sayHi
print(sayHello("Marv"))
print(sayHi("Joy"))
