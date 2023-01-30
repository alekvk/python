import view
import output


# main_dct = {"FI":{"MATH":[6,3,4],"PHISC":[232]},"FI":}
main_dct = {}
student_name = []
lessons = []

def start():

   while True:
      op = view.get_op()
      if op == 1:
         student = view.input_student()
         if student not in student_name:
             main_dct[student] = {}
             student_name.append(student)
             if lessons:
                for less in lessons:
                    main_dct[student][less] = []
      elif op == 2:
         less = view.input_less()
         lessons.append(less)
         for name in student_name:
            main_dct[name][less] = []
      elif op == 3:
         name, less, mark = view.input_mark()
         main_dct[name][less].append(mark)
      elif op == 4:
         print(main_dct)
      elif op == 5:
         name = view.get_name_to_show()
         print(f"Оценки {name} - {main_dct[name]}")
      elif op == 6:
         main_dct2 = view.genDct()
      elif op == 7:
         sub = view.get_sub()
         avr = output.avrSubject(main_dct2, sub)
         print (f"Средн. бал по школе по предмету {sub} равен {avr}")
      elif op == 8:
         name,sub,avr = output.avrOneSub(main_dct2)
         print(f"Средн. оценка ученика {name} по предмету {sub} равна {avr}")
      elif op == 9:
         q,list_name = output.medal(main_dct2)
         print(f"Кол-во учеников претендующих на золотую медаль {q} ")
         print (list_name)
         print("\n")
      elif op == 10:
         output.exportFile(main_dct2)
      elif op == 11:
         print(main_dct2)
      elif op == 12:
         break




