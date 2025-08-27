Test Suite Structure:
---------------------

1. TestBooksCollector Class
   - Tests for add_new_book method
   - Tests for set_book_genre method
   - Tests for get_book_genre method
   - Tests for get_books_genre method
   - Tests for get_books_with_specific_genre method
   - Tests for get_books_for_children method
   - Tests for add_book_in_favorites method
   - Tests for delete_book_from_favorites method
   - Tests for get_list_of_favorites_books method

2. Test Fixtures (in conftest.py)
   - collector: Creates a new BooksCollector instance
   - book_without_genre: Adds a book without a genre
   - book_with_genre: Adds a book with a genre
   - favorite_book: Adds a book to favorites
   - specific_genre: Adds multiple books with different genres

Running the Tests:
------------------
Execute the following command to run all tests:
$ pytest -v tests.py