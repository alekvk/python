def sort_names():
   with open("telephon_book.txt", "r") as file:
       lst = file.readlines()
       lst_with_lst = []
       for line in lst:
           a = line.strip().split(",")
           lst_with_lst.append(a)

       lst_with_lst = sorted(lst_with_lst, key = lambda x: x[1])
       string_ = ""
       for worker in lst_with_lst:
           res = ",".join(worker)
           string_ += res+"\n"
       with open("telephon_book.txt", "w") as file:
           file.write(string_)

def sort_id():
   with open("telephon_book.txt", "r") as file:
           lst = file.readlines()
           lst_with_lst = []
           for line in lst:
               a = line.strip().split(",")
               lst_with_lst.append(a)

           lst_with_lst = sorted(lst_with_lst, key = lambda x: int(x[0]))
           string_ = ""
           for worker in lst_with_lst:
               res = ",".join(worker)
               string_ += res + "\n"
           with open("telephon_book.txt", "w") as file:
               file.write(string_)

