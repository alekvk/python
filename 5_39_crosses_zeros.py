'''
39(2). Создайте программу для игры в ""Крестики-нолики"".
Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту
(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента,
каждый из которого обозначает соответсвующие клетки от 1 до 9),
сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик,
и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
'''
# Функция вывода по три элемента списка в каждой строке
def PrintMap (n):
   i = 0
   while (i < len(n)):
         j = 1
         while (j <= 3):
               print(n[i], end="  ")
               j += 1
               i += 1
         print("")
# Инициалируем список с выигрышными комбинациями


def CheckWin(s):
    winLines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in winLines:
        w = 0
        j = 0
        for j in range (0, 3):
            if (s.find(str(i[j])) != -1):
                w += 1
        if (w == 3):
            return 1
            break
    return 0

map = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = ""
player2 = ""
moves = ""
n1 = 0
n2 = 0
end = 0
flag = 1
step = 0
PrintMap(map)
while (step < 9):
  if (flag == 1):
     n1 = int(input("Ход первого игрока. Введите координату клетки: цифру от 1 до 9  "))
     while (n1 < 1 or n1 > 9):
         n1 = int(input("Введите цифру от 1 до 9  "))
     while ( moves.find(str(n1)) != - 1):
         n1 = int(input("Эта клетка уже занята, введите другую коррдинату  "))
         while (n1 < 1 or n1 > 9):
            n1 = int(input("Введите цифру от 1 до 9  "))

     player1 += str(n1)
     map [n1-1] = "X"
     PrintMap(map)
     if (step >= 4):
        if (CheckWin(player1) == 1):
            print ("Выиграл игрок номер 1")
            break
     moves += str(n1)
     flag = 2


  else:
     n2 = int(input("Ход второго игрока. Введите координату клетки: цифру от 1 до 9  "))
     while (n2 < 1 or n2 > 9):
         n2 =int(input("Введите цифру от 1 до 9  "))
     while (moves.find(str(n2)) != - 1):
         n2 = int(input("Эта клетка уже занята, введите другую коррдинату  "))
         while (n2 < 1 or n2 > 9):
             n2 = int(input("Введите цифру от 1 до 9  "))
     player2 += str(n2)
     map[n2 - 1] = "0"
     PrintMap(map)
     if (step >= 4):
         if (CheckWin(player2) == 1):
             print("Выиграл игрок номер 2")
             break
     moves += str(n2)
     flag = 1
  step += 1
  if (step == 9):
      print ("Ничья")



