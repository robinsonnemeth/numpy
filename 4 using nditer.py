#Exercises using nditer

import numpy as np

def next_exercise():
  print(20*('*'))

a = np.arange(12).reshape(3,4)

#using flatten function
print(f'Exercise 1: ')
for cell in a:
  print(cell)
next_exercise()

print(f'Exercise 2: ')  
for cell in a.flatten():
  print(cell)
next_exercise()

# order C - reads 1 by 1 from left to rigth and line by line
print(f'Exercise 3: ')
for x in np.nditer(a, order='C'):
  print(x)
next_exercise()

print(f'Exercise 4: ')
# order F - reads 1 by 1 from up to down and row by row
for x in np.nditer(a, order='F'):
  print(x)
next_exercise()

print(f'Exercise 5: ')
# flags
for x in np.nditer(a, order='F', flags=['external_loop']):
  print(x)
next_exercise()

print(f'Exercise 6: ')
for x in np.nditer(a, order='F', op_flags=['readwrite']):
  x[...]=x*x
  print(x)
next_exercise()

print(f'Exercise 7: ')
b = np.arange(3,15,4).reshape(3,1)
for x,y in np.nditer([a,b]):
  print(x,y)
