# -*- coding: utf-8 -*-
"""Day4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YAeGbp3ddO08DYVta_OyHV1oqfz5w845
"""

def factorial(num):
    factorial = 1    
    if num < 0:    
        print(" Factorial does not exist for negative numbers")    
    elif num == 0:    
        print("The factorial of 0 is 1")    
    else:    
        for i in range(1,num + 1):    
            factorial = factorial*i    
        print("The factorial of",num,"is",factorial)    


num = int(input("Enter a number: "))
factorial(num)