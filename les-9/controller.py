import view
import model


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:

                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
                index = view.input_index('Введите номер изменяемого контакта ')
                contact = view.change_contact(pb, index)
                model.change_contact(contact, index)
                view.show_message(
                    f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен!')
            case 6:
                search = view.input_search('Введите искомый элемент: ')
                result = model.find_contact(search)
                records = [model.phone_book[index] for index in result]
                view.show_contacts(records, 'Контакты не найдены')
            case 7:
                search = view.input_search('Введите искомый элемент: ')
                model.phone_book = model.delete_contact(
                    search, model.phone_book)
            case 8:
                return
