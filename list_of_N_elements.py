'''
Задайте список из N элементов, заполненных числами из промежутка[-N, N].
Найдите произведение элементов на указанных позициях.Позиции хранятся в
файле file.txt в одной строке одно число.
'''

print('Введите целое положительное  число не равное нулю' )
n = int(input())
numbers = [i for i in range(-n, n + 1)]
print('Элементы списка numbers: ')
print(numbers)

# Задаем список индексов, преобразуем элементы индекса в строки
# и записываем в файл file.txt
list_index = [0, 1, 3, 10, 13]
list = []
for c in list_index:
    list.append(str(c))
data = open('file.txt','w')
with open('file.txt','w') as data:
    for line in list:
        data.write(f"{line}\n")


file = open("file.txt","r")
a = file.readlines()
for i in range(len(a)):
    a[i] = int(a[i].strip())
print('Индексы в файле file.txt')
print(a)

multi = 1
for i in range(len(a)):
    multi *= numbers[a[i]]
print(multi)















