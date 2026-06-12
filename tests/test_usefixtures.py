import pytest

@pytest.fixture
def clear_books_database():
    print  ("FIXTURE удаляем все данные из БД")

@pytest.fixture
def fill_books_database():
    print("FIXTURE Создаем новые данные из БД")

@pytest.mark.usefixtures("fill_books_database")
def test_read_all_books_in_library():
    print("Reading all books in library")

