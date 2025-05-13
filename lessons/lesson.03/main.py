from contact import Contact
from phonebook import PhoneBook
from notes import Notes


def print_items(item):
    item.list_items()


def main():
    my_phonebook = PhoneBook()

    try:
        contact1 = Contact("Иван1", "+79261234567", "ivan@mail.ru")
        print('Контакт создан успешно')
    except ValueError as e:
        print(e)

    try:
        contact2 = Contact("Боб1", "+79112223344", "bob@mail.ru")
        print('Контакт создан успешно')
    except ValueError as e:
        print(e)

    contact3 = Contact("Боб1", "+79111113377", "admin@mail.ru")

    my_phonebook.add_contact(contact1)
    my_phonebook.add_contact(contact2)
    my_phonebook.add_contact(contact3)


    my_phonebook2 = PhoneBook()

    try:
        contact4 = Contact("Иван2", "+79261234567", "ivan@mail.ru")
        print('Контакт создан успешно')
    except ValueError as e:
        print(e)

    try:
        contact5 = Contact("Боб2", "+79112223344", "bob@mail.ru")
        print('Контакт создан успешно')
    except ValueError as e:
        print(e)

    contact6 = Contact("Боб2", "+79111113377", "admin@mail.ru")

    my_phonebook2.add_contact(contact4)
    my_phonebook2.add_contact(contact5)
    my_phonebook2.add_contact(contact6)


    # print('*' * 50)
    # my_phonebook.list_contacts()
    # print('*' * 50)
    # print(contact2)
    # print('*' * 50)
    # print(repr(contact2))
    # print('*' * 50)
    # print(my_phonebook)

    # print(contact1 == contact2)
    # print(contact3 == contact2)

    # print(len(my_phonebook))

    # print(my_phonebook)

    # print(my_phonebook[0])
    # # my_phonebook[1] = 3
    # my_phonebook[0] = contact3
    #
    # print(my_phonebook[0])

    # print(my_phonebook)
    # del my_phonebook[2]
    # print(my_phonebook)


    # print(my_phonebook)


    # new_my_book = my_phonebook + my_phonebook2
    # print(new_my_book)
    #
    # my_phonebook += my_phonebook2
    #
    # print(my_phonebook)


    # note = Notes()
    # note.add_notes('Сделать ДЗ')
    # note.add_notes('Купить хлеб')
    #
    # print_items(my_phonebook)
    # print_items(note)


    print(Contact.is_valid_phone("799999999"))
    print(Contact.is_valid_phone("+79111113377999"))
    print(Contact.is_valid_phone("+79111113377"))

    contact8 = Contact.from_string('Боб7, +79112223344, bob1@mail.ru')
    print(contact8)
    print(type(contact8))
if __name__ == '__main__':
    main()
