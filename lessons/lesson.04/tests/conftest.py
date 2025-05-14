import pytest
from contact import Contact


@pytest.fixture
def my_contact():
    return Contact("Bob", "+79997775533", "bob@mail.ru")


@pytest.fixture
def my_contact_2():
    return Contact("Ann", "+73337775533", "Ann@mail.ru")