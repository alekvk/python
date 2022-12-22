import math
print('Введите вещественное число')
n = (input())
# Определяем длину всего числа как строки (вместе с точкой)
lTotal = len(n)
# Преобразуем строку в тип float
n = float (n)
# Определяем длину дробной части числа
# Длину целой части числа вычисляем посредством десятичного логарифма: int(math.log10(n))+1
lFract = lTotal - int(math.log10(n)) - 2
# Умножаем исходное число на 10 в степени lFract, т.е получаем целое число с теми же цифрами
n = int(n * math.pow(10,lFract))
print(n)
# Далее работаем с целым числом
r = 1
i = 1
sum = 0
numbers = []
while (r > 0):
     r = int((n/i)%10)
     sum += r
     numbers.append(r)
     i*=10
numbers.reverse()
print(numbers)
print(f'Сумма цифр равна {sum}')


