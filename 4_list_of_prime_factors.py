'''
Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
'''
multipliers = []
n = int(input("Введите целое число  "))
s = 0
while (s == 0):
    for i in range(2, 99):
        if (n % i == 0  and i != n):
            multipliers.append(i)
            break
    if (n % i != 0):
        multipliers.append(n)
        s = 1
    n = n // i

print(multipliers)

