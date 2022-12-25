'''
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

numbers = [1.4, 6, 1.1, 1.2, 3.1, 5, 10.01, 8]
i = 0
minFract = numbers[i] % 1
indexMin = i
maxFract = numbers[i] % 1
indexMax = i
i = 1
while (i < len(numbers)):
     n = numbers[i] % 1
     if ((minFract > n and n != 0) or minFract == 0):
         minFract = n
         indexMin = i
     elif  (maxFract < n ):
         maxFract = n
         indexMax = i
     i += 1
print(numbers)
print(f'Индекс элемента с минимальным значением дробной части -  {indexMin}')
print(f'Индекс элемента с максимальным значением дробной части -  {indexMax}')
print(f'Разница между элементами  {round((maxFract - minFract),2)}')






