'''
3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

'''

import random

def Coeff(min = 0, max = 100):
    return (random.randint(min, max))

k = int(input('Введите положительное число степени многочлена   '))
if k < 0: k = -k

# Формируем старший член многочлена
n = Coeff(1)
if n > 1:
   member1 = str(n) + "*x**" + str(k)
else:
   member1 = "x**" + str(k)

# Формируем член многочлена со степенью 1
n = Coeff()
if n > 1:
   member2 = " + " + str(n) + "*x"
elif n == 1:
   member2 = " + " + "x"
else:
    member2 = ""

# Формируем свободный член многочлена
n = Coeff()
if n > 0:
   member3 = " + " + str(n)  
else: 
   member3 = ""     
   
polynomial = member1 
k = k - 1
while (k > 1):
    n = Coeff()
    if (n > 1):
        line = str(n) + '*x**' + str(k)
    elif (n == 1):
        line = 'x**' + str(k)
    else:
        line = ""
    if line != "":
        polynomial += " + " +  line
    k = k - 1

polynomial = polynomial + member2 + member3 + " = 0"
print(polynomial)

with open("4_file_polynomial.txt", "w") as data:
   data.write(polynomial)

