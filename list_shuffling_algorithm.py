#Реализуйте алгоритм перемешивания списка.

#Задаем список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
import random
print('Элементы списка до перемешивания:')
print(numbers)

# Инициализируем числом 2 коэффициент "надежности" перемешивания (число проходов по списку)
k = 2
for c in range (k):
    i = 0
    for d in numbers:
        index = random.randint(0, len(numbers)-1)
        temporary = numbers[index]
        numbers[index] = d
        numbers[i] = temporary
        i+=1

print('Элементы списка после перемешивания:')
print(numbers)



