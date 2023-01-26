
def print_table():
    with open("telephon_book.txt", "r") as file:
        for i in file.readlines():
            print(i, end = "")

def print_only_name():
    with open("telephon_book.txt","r") as file:
        lst = file.readlines()
        for line in lst:
            a = line.split(",")
            print(f"Имя - {a[1]}, Фамилия - {a[2]}")

