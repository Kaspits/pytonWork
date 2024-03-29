phone_book = []
path = 'C:\\Users\\PC\\Desktop\\PytonWork\\pytonWork\\les-9\\phone.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)


def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(list(contact.values())))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_phone_book():
    return phone_book


def add_contact(contact: dict):
    phone_book.append(contact)


def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)


def find_contact(search: str) -> list[int]:
    result = []
    for contact_index, contact in enumerate(phone_book):
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact_index)
    return result


def delete_contact(search: str, phone_book: list[str]):
    match_indexes = find_contact(search)
    phone_book = [record for index, record in enumerate(
        phone_book) if index not in match_indexes]
    return phone_book
