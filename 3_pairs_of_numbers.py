'''
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
def Pair (list):
  if (len(list) %2 == 0):
      n = len(list)/2
  else:
      n = int(len(list)/2) + 1
  i = 0
  listPair = []
  while (i < n):
    listPair.append(list[i] * list[len(list) - 1 - i])
    i += 1
  return listPair

numbers_1 = [2, 4, 5, 9, 3]
numbers_2 = [2, 4, 9, 3]

print(numbers_1)
print(Pair(numbers_1))
print(numbers_2)
print(Pair(numbers_2))



