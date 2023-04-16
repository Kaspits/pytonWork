import phone_book

pb = phone_book.PhoneBook(
    "C:\\Users\\PC\\Desktop\\PytonWork\\pytonWork\\les-10\\phone_db.txt"
)

while True:
    print(pb.main_menu())
    coice = int(input("Выберите пункт меню: "))
    match coice:
        case 1:
            print(pb)
        case 2:
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            comment = input("Введите комментарий: ")
            pb.new_contact(name, phone, comment)
        case 3:
            word = input("Введите поисковый запрос: ")
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input("Введите индекс контакта, который будем изменять: "))
            name = input("Введите имя (или ничего, если без изменений): ")
            phone = input("Введите телефон (или ничего, если без изменений): ")
            comment = input("Введите комментарий (или ничего, если без изменений): ")
            pb.change(index - 1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input("Введите индекс контакта, который будем удалять: "))
            pb.delete(index - 1)
        case 6:
            pb.save()
        case 7:
            break
