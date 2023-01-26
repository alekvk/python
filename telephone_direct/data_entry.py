

def add_phoneNumber():
    id = input("Введите id записи  ")
    name = input("Введите имя  ")
    lastname = input("Введите фамилию  ")
    number = input("Введите телефонный номер  ")
    comments = input("Введите комментарий  ")
    line = f"{id},{name},{lastname},{number},{comments}\n"
    with open ("telephon_book.txt", "a") as file:
        file.write(line)
    file.close()
    print("Данные сохранены")
