# from functools import total_ordering


# @total_ordering
class Contact:
    """Класс, описывающтй контакт телефонного справочника."""

    def __init__(self, name: str, phone: str, email: str):
        """Инициализация контакта."""
        if not phone.startswith("+7") or len(phone) != 12:
            raise ValueError('Телефон должен начинаться с +7 и быть 12 символов')
        self.name = name
        self.phone = phone
        self.email = email

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name

    def __lt__(self, other):
        """<"""
        pass

    def __gt__(self, other):
        """>"""
        pass

    def __le__(self, other):
        """<="""
        pass

    def __ge__(self, other):
        """>="""
        pass

    def __ne__(self, other):
        """!="""
        pass




    def __str__(self):
        return f'Имя: {self.name}, Телефон: {self.phone}, Email: {self.email}'

    def __repr__(self):
        return f'Contact(name=({self.name}), phone=({self.phone}), email=({self.email})'


    @staticmethod
    def is_valid_phone(phone):
        if not phone.startswith("+7"):
            return False
        elif len(phone) != 12:
            return False
        return True

    @classmethod
    def from_string(cls, contact_str):
        try:
            name, phone, email = contact_str.strip().split(', ')
        except ValueError:
            raise ValueError('Некорректный формат')
        return cls(name, phone, email)


if __name__ == '__main__':
    print("Запустили contact")