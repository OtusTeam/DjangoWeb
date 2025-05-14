import pytest
from contact import Contact


# @pytest.fixture
# def my_contact():
#     return Contact("Bob", "+79997775533", "bob@mail.ru")


def test_create_contact(my_contact):
    contact1 = Contact("Bob", "+79997775533", "bob@mail.ru")
    contact1 = my_contact
    assert contact1.name == "Bob"
    assert contact1.phone == "+79997775533"
    assert contact1.email == "bob@mail.ru"


def test_create_contact_raises_exception():
    # with pytest.raises(ValueError, match=r'Телефон должен начинаться с +7 и быть 12 символов'):
    with pytest.raises(ValueError):
        Contact("Bob", "89997775533", "bob@mail.ru")


def test_contact_str(my_contact):
    # contact1 = Contact("Bob", "+79997775533", "bob@mail.ru")
    contact1 = my_contact
    result = str(contact1)
    expected = 'Имя: Bob, Телефон: +79997775533, Email: bob@mail.ru'
    assert result == expected


def test_contact_repr(my_contact):
    # contact1 = Contact("Bob", "+79997775533", "bob@mail.ru")
    contact1 = my_contact
    result = repr(contact1)
    expected = 'Contact(name=(Bob), phone=(+79997775533), email=(bob@mail.ru)'
    assert result == expected


@pytest.mark.parametrize(
    "number, is_valid",
    [
        ('+79997775533', True),
        ('79997775533', False),
        ('+7899777153312', False),
        ('89997775533', False),
        ('+79997775511', True),
    ])
def test_is_valid_phone(number, is_valid):
    assert Contact.is_valid_phone(number) is is_valid


def test_print_contact(my_contact, capsys):
    contact1 = Contact("Bob", "+79997775533", "bob@mail.ru")
    print(contact1)
    result = 'Имя: Bob, Телефон: +79997775533, Email: bob@mail.ru'
    captured = capsys.readouterr()
    assert 'Bob' in captured.out