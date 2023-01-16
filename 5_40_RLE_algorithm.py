'''
40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные данные: 111112222334445. Выходные данные: 5142233415
Входные данные: AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE. Выходные данные: 6A1F2D7C1A17E
(5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
Модуль восстановления работет в обратную сторону -
из строки выходных данных, получить строку входных данных.
'''

# Функция сжатия
def RleCompr(s):
  rleString = ""
  i = 0
  while (i < len(s)):
     count = 1
     a = s[i]
     i += 1
     while (i < len(s) and a == s[i]):
             count += 1
             i += 1
     if (count > 1):
        rleString += str(count) + str(a)
     else:
         rleString += "1" + str(a)
  return rleString

#  Функция восстановления
def Decompr(s):
    i = 0
    d = ""
    a = 0
    while (i < len(s)):
         n = ""
         while (s[i].isdigit()):
              n += str(s[i])
              i += 1
         a = int(n)
         st = s[i]
         d += st * a
         i += 1
    return d

# Сжимаем текст из файла 5_input_data.txt и помещаем его в файл 5_output_data.txt
input = open('5_input_data.txt', 'r')
inpString = input.read()
output = open('5_output_data.txt', 'w')
output.write(RleCompr(inpString))
output.close()

# Восстанавливаем текст из файла 5_output_data.txt и помещаем его в файл 5_decompr.txt
input = open('5_output_data.txt', 'r')
inpString = input.read()
output = open('5_decompr.txt', 'w')
output.write(Decompr(inpString))
output.close()



