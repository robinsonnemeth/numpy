# Exercises to check functionality - slicing arrays
import numpy as np

a = np.array([6,7,8])
print(f'exercise 1: {a[0:2]}')
print(f'exercise 2: {a-1}')
print(f'exercise 3: {a[-1]}')

a = np.array([[6,7,8], [1,2,3],[9,3,2]])
print(f'exercise 4: {a}')
print(f'exercise 5: {a[1,2]}')
print(f'exercise 6: {a[0:2,2]}')
print(f'exercise 7: {a[-1]}')
print(f'exercise 8: {a[-1,0:2]}')
print(f'exercise 9: {a[:,1:3]}')

for row in a:
    print(f'exercise 10: {row}')

for cell in a.flat:
    print(f'exercise 11: {cell}')

a = np.arange(6).reshape(3,2)
print(f'exercise 12: {a}')
b = np.arange(6,12).reshape(3,2)
print(f'exercise 13: {b}')
print(f'exercise 14: {np.vstack((a,b))}')
print(f'exercise 15: {np.hstack((a,b))}')

a = np.arange(30).reshape(2,15)
print(f'exercise 16: {a}')
print(f'exercise 17: {np.hsplit(a,3)}')
print(f'exercise 18: {np.vsplit(a,2)}')

a = np.arange(12).reshape(3,4)
b = a>4
print(f'exercise 19: {b}')
print(f'exercise 20: {a[b]}')
a[b] = -1
print(f'exercise 21: {a}')



