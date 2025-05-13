from contact import Contact

class PhoneBook:
    """Класс для управления справочником"""

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            print(f'{contact.name}, {contact.phone}, {contact.email}')

    def __str__(self):
        result = ''
        for contact in self.contacts:
            result += f'{contact.name}, {contact.phone}, {contact.email}\n'
        return result

    def __len__(self):
        return len(self.contacts)

    def __getitem__(self, index):
        return self.contacts[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Contact):
            raise ValueError("Значение должно быть объектом Contact")
        self.contacts[index] = value

    def __delitem__(self, key):
        del self.contacts[key]

    def __add__(self, other):
        if not isinstance(other, PhoneBook):
            raise TypeError("Можно складывать только с другими PhoneBook")
        new_phonebook = PhoneBook()
        new_phonebook.contacts = self.contacts + other.contacts
        return new_phonebook

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def list_items(self):
        print('Список контактов')
        for contact in self.contacts:
            print(f'{contact.name}, {contact.phone}, {contact.email}')



if __name__ == '__main__':
    print("Запустили phonebook")