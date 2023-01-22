'''
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
'''

# Функция StrFromDict принимает на вход словарь (ключ - показатель степени,
# значение - коэффициент члена многочлена) и возвращает строку многочлена
def StrFromDict(d):
    polynomial = ""
    f1 = d.items()
    for i in range(len(d) - 1, -1, -1):
        f = list(f1)[i]
        key = f[0]
        value = f[1]
        if (int(key) > 1):
            if (value == 1 and i == len(d) - 1):
                polynomial += "x**" + key
            elif (value > 1 and i == len(d) - 1):
                polynomial += str(value) + "*x**" + key
            elif (value == 1):
                polynomial += "+" + "*x**" + key
            elif (value > 1):
                polynomial += "+" + str(value) + "*x**" + key
            elif (value == -1):
                polynomial += "-" + "x**" + key
            elif (value < -1):
                polynomial += str(value) + "*x**" + key
            else:
                polynomial = polynomial

        elif (int(key) == 1):
            if (value == 1 and i == len(d) - 1):
                polynomial += "x"
            elif (value > 1 and i == len(d) - 1):
                polynomial += str(value) + "*x"
            elif (value == 1):
                polynomial += "+" + "*x"
            elif (value > 1):
                polynomial += "+" + str(value) + "*x"
            elif (value == -1):
                polynomial += "-" + "x"
            elif (value < -1):
                polynomial += str(value) + "*x"
            else:
                polynomial = polynomial

        else:
            if (value > 1):
                polynomial += "+" + str(value)
            elif (value <= -1):
                polynomial += str(value)
            else:
                polynomial += polynomial

    polynomial += "=0"
    return polynomial

# Функция DictFromStr принимает на вход строку многочлена
# и возвращает  словарь (ключ - показатель степени, # значение - коэффициент члена многочлена)
def DictFromStr(s):
  dict = {}
  # Убираем  "=0"
  s = s.replace('=0', '')
  # Находим свободный член многочлена (при наличии)
  value = 0
  val =""
  if ((s[-1]).isdigit()):
     val = s[-1]
     for i in range((len(s) - 2), 0, -1):
       if (s[i].isdigit()):
           val += s[i]
       else:
           if (s[i] != "*"):
               if (s[i] == "+"):
                   val = val[::-1]
                   value = int(val)
               else:
                   val = val[::-1]
                   value = -int(val)
               s = s[0:i]
           else:
               value = 0
           break
  else:
      value = 0
  if (value != 0):
    dict['0'] = value

  # Находим член многочлена со степенью 1 (при наличии)
  value = 0
  val = ''
  if ((s[-1]) == "x"):
     if ((len(s) -1) == 0):
         value = 1
         s = s[0:-1]
     elif(s[-2] == "+"):
         value = 1
         s = s[0:-2]
     elif(s[-2] == "-"):
         value = -1
         s = s[0:-2]
     else:
         for i in range((len(s) - 3), -1, -1):
             if (s[i].isdigit()):
                 val += s[i]
                 if (i == 0):
                     val = val[::-1]
                     value = int(val)
                     s = s[0:i]
                     break
             else:
                 if (s[i] == "+"):
                         val = val[::-1]
                         value = int(val)
                 else:
                         val = val[::-1]
                         value = -int(val)
                 s = s[0:i]
                 break
  else:
      value = 0
  if (value != 0):
    dict['1'] = value

  # Находим члены многочлена со степенью n, где n не равно 0 или 1
  for i in range((len(s) - 1), 0, -1):
        val = ''
        value = 0
        key = ''
        for j in range((len(s) - 1), -1, -1):
            if (s[j].isdigit()):
                key += s[j]
            else:
                key = key[::-1]
                break
        s = s[0:j-2]
        k = j - 2
        if (k == 0):
             value = 1
        elif (s[k - 1] == "+"):
            k = k - 1
            value = 1
        elif (s[k - 1] == "-"):
            k = k - 1
            value = - 1
        else:
            k = k - 2
            while (k >= 0):
                if(s[k].isdigit()):
                      val += s[k]
                      if(k == 0): value = int(val[::-1])
                elif(s[k]=="+"):
                      value = int(val[::-1])
                      break
                else:
                      val = val[::-1]
                      value = - int(val)
                      break
                k = k - 1
        if (k > 0):
            s = s[0:k]
        else:
             dict[key] = value
             break
        dict[key] = value
  return dict

# Функция MergDict объединяет два словаря. Значения для одинаковых ключей складываются.
def MergDict (d1,d2):
    k = set(list(d1.keys())+list(d2.keys()))
    d = {}
    for i in k:
        value1 = d1.get(i)
        value2 = d2.get(i)
        if value1 == None:
            value = value2
        elif value2 == None:
            value = value1
        else:
            value = value1 + value2
        d[i] = value
    d = dict(sorted(d.items()))
    return d

input1 = open('4_polynomial_1.txt', 'r')
input2 = open('4_polynomial_2.txt', 'r')
aString1 = input1.read()
aString2 = input2.read()
print(aString1)
print(aString2)

print("Словари, полученные  из многочленов")
dict1 = DictFromStr(aString1)
print(dict1)
dict2 = DictFromStr(aString2)
print(dict2)

# Объединение двух словарей
dict3 = MergDict (dict1, dict2)

# Выводим сумму многочленов
polynom = StrFromDict(dict3)
print("Сумма многочленов")
print(polynom)

output = open('4_sum_polinom.txt', 'w')
output.write(polynom)

































