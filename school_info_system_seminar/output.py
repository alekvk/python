import view

# Вывод средней оценки ученика по одному предмету
def avrOneSub(dct):
    name = input("Введите имя и через один пробел фамилию ученика-")
    while name not in dct:
        print ("Ученик с указанным именем и фамилией отсутствует в списке")
        name = input("Введите имя и через один пробел фамилию ученика-")
    value = dct[name]
    print(value)
    sub = view.get_sub()
    while sub not in value:
        print ("Введите правильный номер предмета")
        sub = view.get_sub()
    grades = value[sub]
    sum = 0
    for i in range(len(grades)):
        sum = sum + grades[i]
    avr = sum / len(grades)
    return name, sub, avr

# Вывод среднего балла по школе по конкретному предмету
def avrSubject(dct, n):
    sumDct = 0
    quant = 0
    for a in dct.values():
        for key, value in a.items():
            if key == n:
                sum = 0
                for i in value:
                    sum = sum + i
                sumDct += sum
                quant += len(value)
    avr = sumDct / quant
    return (avr)

# Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
def  medal(dct):
    q = 0
    list_name = []
    name = ""
    for key, value in dct.items():
        name = key
        medal = True
        for sub, grades in value.items():
            for i in grades:
                if i < 4:
                    medal = False
                    break
            if medal == False:
                break
        if medal == True:
            q += 1
            list_name.append(name)

    return q, list_name

# Хранение в файле, и импорт из файла
def exportFile(dct):
     file = open("dct.txt", "w")
     file.write("")
     file = open("dct.txt", "a")
     i = 1
     for key,value in dct.items():
          l = f"{str(i)} {key} {value}"
          file.write(l + "\n")
          i += 1

