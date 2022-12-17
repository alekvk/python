# 1.	Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ # Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print ('Проверяем истинность ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ')
# Инициализируем нулем индикатор истинности
a = 0
# Запускаем цикл перебора возможных значений предикат
for x in range(2):
    for y in range(2):
        for z in range(2):
            left = not(x or y or z)
            right = (not x) and (not y) and (not z)
            print (f'x = {x}, y = {y}, z = {z},  ¬(X ⋁ Y ⋁ Z)= {left},  ¬X ⋀ ¬Y ⋀ ¬Z = {right}')
            if left != right:
                ++a
if a == 0:
    print('Утвеждение ¬(X ⋁ Y ⋁ # Z) = ¬X ⋀ ¬Y ⋀ ¬Z)  истинно')
else:
    print('Утвеждение ¬(X ⋁ Y ⋁ # Z) = ¬X ⋀ ¬Y ⋀ ¬Z)  ложно')

