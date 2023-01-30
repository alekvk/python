from random import randint

def get_op():
    op = int(input (" 1 - добавить студента, 2 - добавить предмет, 3 - добавить оценку, 4 - показ списка, "
                    "5 - показ конк список, \n 6 - генератор журнала, 7 - средн. бал по школе по конкр. предмету"
                    " 8 - средн.оценка ученика по одному предмету, \n 9 - кол-во учеников претендующих на золотую медаль,"
                    "10 - выгрузка журнала в файл, 11 - показ списка из 100 учеников, 12 - выход "))
    return op

def get_sub():
    d = {'1':'BIOL', '2':'CHEM', '3':'LITERAT', '4':'MATH', '5':'RUSSIAN'}
    n = int(input("Введите номер предмета: BIOL - 1, CHEM - 2, LITERAT - 3, MATH - 4, RUSSIAN - 5  "))
    if (n < 1 or n > 5):
        n = int(input("Введите номер, соответствующий предмету: \n"
                " BIOL - 1, CHEM - 2, LITERAT - 3, MATH - 4, RUSSIAN - 5  "))
    else:
       return d[str(n)]

def input_student():
    name = input("Введите имя и фамилию ")
    return name

def input_less():
    less = input("Введите предмет ")
    return less

def input_mark():
    name = input("Введите имя ")
    less = input("Введи предмет ")
    mark = input("Введите оценку ")
    return name, less, mark

def get_name_to_show():
    name = input("Введите имя для просмотра оценок ")
    return name

listName = ['Aleksandr', 'Aleksey', 'Andrey', 'Andron', 'Vladimir','Dmitriy', 'Mihail', 'Nikolai','Oleg','Sergey',
            'Victor', 'Valentin']
listSurname = ['Aminov','Apin','Aronov', 'Asin', 'Azin', 'Barinov', 'Belugin', 'Cedenko', 'Civilin', 'Duzev', 'Faminov',
               'Frolov', 'Gamin', 'Guseev', 'Guzin']
listSubject = ['BIOL','CHEM','LITERAT','MATH', 'RUSSIAN']

def getRandom(list):
    return list[randint(0, len(list) - 1)]

# Генерация сразу ста учеников и записи их в журнал
def genDct():
   main_dct = {}
   student_name = []
   i = 0
   while i < 100:
         name = getRandom(listName)
         surname = getRandom(listSurname)
         student = name + " " + surname
         if student not in student_name:
             main_dct[student] = {}
             student_name.append(student)
             i += 1
             j = 0
             subjects = []
             while j < 2:
                subject = getRandom(listSubject)
                if subject not in subjects:
                    subjects.append(subject)
                    j += 1
                    main_dct[student][subject] = {}
                    k = 0
                    listMark = []
                    while k < 3:
                        mark = randint(3,5)
                        listMark.append(mark)
                        k += 1
                    main_dct[student][subject] = listMark
   return main_dct


