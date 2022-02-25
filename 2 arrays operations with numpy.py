# Exercises performing operations with arrays
import numpy as np

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
print(f'Exercise 1 = {a1+a2}')
print(f'Exercise 2 = {a2-a1}')
print(f'Exercise 3 = {a1*a2}')
print(f'Exercise 4 = {a1/a2}')

a = np.array([5,6,9])
print(f'Exercise 5 = {a[0]}')
print(f'Exercise 6 = {a[1]}')

a=np.array([[1,2],[3,4],[5,6]])
print(f'Exercise 7 = {a.ndim}')
print(f'Exercise 8 = {a.itemsize}')
print(f'Exercise 9 = {a.size}')
print(f'Exercise 10 = {a.dtype}')

a=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(f'Exercise 11 = {a.dtype}')
print(f'Exercise 12 = {a.itemsize}')
print(f'Exercise 13 = {a}')
print(f'Exercise 14 = {a.shape}')
print(f'Exercise 15 = {a.reshape(2,3)}')

a=np.zeros((3,4))
print(f'Exercise 16 = {a}')

a=np.ones((3,4))
print(f'Exercise 17 = {a}')

a=np.arange(1,5)
print(f'Exercise 18 = {a}')

a=np.arange(1,5,2)
print(f'Exercise 19 = {a}')

a=np.linspace(1,5,10)
print(f'Exercise 20 = {a}')
print(f'Exercise 21 = {a.reshape(10,1)}')
print(f'Exercise 22 = {a.ravel()}')

a = np.array([[1,2],[2,3],[4,5]])
print(f'Exercise 23 = {a.min()}')
print(f'Exercise 24 = {a.max()}')
print(f'Exercise 25 = {a.sum()}')
print(f'Exercise 26 = {a.sum(axis=0)}')
print(f'Exercise 27 = {a.sum(axis=1)}')
print(f'Exercise 28 = {np.sqrt(a)}')

b = np.array([[6,7],[8,9],[10,11]])
print(f'Exercise 29 = {a+b}')
print(f'Exercise 30 = {a*b}')
print(f'Exercise 31 = {a/b}')
print(f'Exercise 32 = {a-b}')
