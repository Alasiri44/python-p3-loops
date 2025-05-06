#!/usr/bin/env python3
import math

def happy_new_year():
   for i in range(10, 0, -1):
       print(i)
   else:
       print("Happy New Year!")

def square_integers(int_list):
    return [integer * integer for integer in int_list]

def fizzbuzz():
    for i in range(1, 101):        
        if(math.remainder((i/3), 5) == 0):
            print("FizzBuzz")
        elif(math.remainder(i, 3) == 0):
            print("Fizz")
        elif(math.remainder(i, 5) == 0):
            print("Buzz")
        else:
            print(i)
        
