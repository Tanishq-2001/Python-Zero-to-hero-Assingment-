# -*- coding: utf-8 -*-
"""Day6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uGxmpcQKqeQl7J1Z3CdqkrzwhHfE11QD
"""

def decorators(fun):

  def deno(num1, num2):
    if num1 < num2:
      num1,num2 = num2,num1
      return fun(num1,num2)
    else:
      return fun(num1,num2)

def div(num1, num2):
	return  num1 // num2

num1 =int(input("Enter two Nunbers: "))
num2 =int(input("Enter two Nunbers: "))
print(num1,num2)


a = decorators(div)

print(a)

def decorators(fun):
	def deno(nbr1, nbr2):
		if nbr1 < nbr2 :
			nbr1, nbr2 = nbr2, nbr1
		return fun(nbr1, nbr2)
	return deno
	
@decorators
def div(nbr1, nbr2):
	return  nbr1 // nbr2

nbr1 =int(input("Enter the nbr: "))
nbr2 =int(input("Enter the nbr: "))
print(nbr1,nbr2)


print(div(nbr1, nbr2))



