from main import BooksCollector
import pytest

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def book_without_genre(collector):
    collector.add_new_book('Книга без жанра')
    return collector
    
@pytest.fixture
def book_with_genre(collector):
    collector.add_new_book('Ужасный ужас в кошмарном кошмаре')
    collector.set_book_genre('Ужасный ужас в кошмарном кошмаре', 'Ужасы')
    return collector

@pytest.fixture
def specific_genre(collector):
    books = [
            ['Фантастическая книга', 'Фантастика'],
            ['Учебник по python 3.0', 'Ужасы'],
            ['Смешная книга', 'Комедии'],
            ['По следам книги', 'Детективы'],
            ['Книга в стране чудес', 'Мультфильмы']
        ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

@pytest.fixture
def favorite_book(collector):
    collector.add_new_book('Самая любимая книга')
    collector.add_book_in_favorites('Самая любимая книга')
    return collector
    