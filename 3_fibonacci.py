'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

def Fibonacci (x):
    if x >= 0:
        if x == 0:
            return 0
        elif (x == 1 or x == 2):
            return 1
        else:
            return Fibonacci(x - 1) + Fibonacci(x - 2)
    if x < 0:
        if x == -1:
            return 1
        elif x == -2:
            return -1
        else:
            return Fibonacci(x + 2) - Fibonacci(x + 1)

n = int (input('Введите целое положительное число  '))
if n < 0:
    n = -n
for i in range(-n, n + 1):
    print(Fibonacci(i), end = " ")
