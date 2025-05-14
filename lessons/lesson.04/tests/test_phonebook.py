import pytest
from contact import Contact
from phonebook import PhoneBook


def test_phonebook_add_contact(my_contact, my_contact_2):
    pb = PhoneBook()
    pb.add_contact(my_contact)
    assert len(pb) == 1
    pb.add_contact(my_contact_2)
    assert len(pb) == 2