from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
    #     создаем экземпляр (объект) класса BooksCollector
    #    collector = BooksCollector()

    #     добавляем две книги
    #    collector.add_new_book('Гордость и предубеждение и зомби')
    #    collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #    assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    # 1) Тесты метода add_new_book()
    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book('Новая книга')
        assert 'Новая книга' in collector.books_genre
    
    @pytest.mark.parametrize('book_name, expected', [
                                                      ['k', True],
                                                      ['k'*40, True],
                                                      ['k'*41, False],
                                                      ['', False],
                                                    ]
                            )
    def test_add_new_book_border_values(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected
          
    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Дубликат')
        collector.add_new_book('Дубликат')
        assert 'Дубликат' in collector.books_genre and len(collector.books_genre) == 1
    
    # 2) Тесты метода set_book_genre()
    def test_set_book_genre_book_in_list_genre(self, book_without_genre):
        book_without_genre.set_book_genre('Книга без жанра', 'Фантастика')
        assert book_without_genre.get_book_genre('Книга без жанра') == 'Фантастика'
    
    def test_set_book_genre_book_not_in_book_genre_list(self, book_without_genre):
        book_without_genre.set_book_genre('Книга, которой нет', 'Детективы')
        assert book_without_genre.get_book_genre('Книга, которой нет') is None
        
    def test_set_book_genre_not_in_list_genre(self, book_without_genre):
        book_without_genre.set_book_genre('Книга без жанра', 'Жанр, которого нет')
        assert book_without_genre.get_book_genre('Книга без жанра') == ''
        
    # 3) Тесты метода get_book_genre()
    @pytest.mark.parametrize('book_name, expected_genre', [
                                                            ['Фантастическая книга', 'Фантастика'],
                                                            ['Учебник по python 3.0', 'Ужасы'],
                                                            ['Смешная книга', 'Комедии'],
                                                            ['По следам книги', 'Детективы'],
                                                            ['Книга в стране чудес', 'Мультфильмы']        
                                                          ]
                                )
    def test_get_book_genre_exist_book(self, specific_genre, book_name, expected_genre):
        assert specific_genre.get_book_genre(book_name) == expected_genre
       
    def test_get_book_genre_empty_books_genre_list(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None
        
    # 4) Тесты метода get_books_with_specific_genre()
    def test_get_books_with_specific_genre_books_exists(self, specific_genre):
        assert specific_genre.get_books_with_specific_genre('Ужасы') == ['Учебник по python 3.0']
    
    def test_get_books_with_specific_genre_no_books(self, collector):
        assert collector.get_books_with_specific_genre('Комедии') == []
    
    # 5) Тесты метода get_books_genre()
    def test_get_books_genre_empty(self, collector):
        assert collector.get_books_genre() == {}
    
    def test_get_books_genre_with_books(self, specific_genre):
        books = specific_genre.get_books_genre()
        assert len(books) == 5
        assert 'По следам книги' in books
        assert books['По следам книги'] == 'Детективы'
    
    # 6) тесты метода get_books_for_children()
    def test_get_books_for_children(self, specific_genre):
        books_for_children = specific_genre.get_books_for_children()
        assert 'Книга в стране чудес' in books_for_children # Проверяем наличие книг для детей в списке книг для детей
        assert 'Учебник по python 3.0' not in books_for_children # Проверяем отсутствие книг с возрастным ограничением в списке книг для детей
    
    # 7) Тесты метода add_book_in_favorites()
    def test_add_book_in_favorites_book_in_list_genre(self, book_without_genre):
        book_without_genre.add_book_in_favorites('Книга без жанра')
        assert 'Книга без жанра' in  book_without_genre.get_list_of_favorites_books()
        
    def  test_add_book_in_favorites_twice(self, favorite_book):
         favorite_book.add_book_in_favorites('Самая любимая книга')
         assert favorite_book.get_list_of_favorites_books().count('Самая любимая книга') == 1
    
    # 8) Тесты метода delete_book_from_favorites
    def test_delete_book_from_favorites_exist(self, favorite_book):
        favorite_book.delete_book_from_favorites('Самая любимая книга')
        assert 'Самая любимая книга' not in favorite_book.get_list_of_favorites_books()
        
    def test_delete_book_from_favorites_not_in_favorites(self, collector):
        collector.delete_book_from_favorites('Самая нелюбимая книга')
        assert 'Самая нелюбимая книга' not in collector.get_list_of_favorites_books()
    
    # 9) Тесты метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_with_favorite_book(self, favorite_book):
        assert 'Самая любимая книга' in favorite_book.get_list_of_favorites_books()
    
    def test_get_list_of_favorites_books_without_favorite_book(self, collector):
        assert collector.get_list_of_favorites_books() == []