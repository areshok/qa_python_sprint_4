class TestBooksCollector:
    "Тест кейс BooksCollector"

    def add_book_adng_genre(self, bookcls, name, genre):
        bookcls.add_new_book(name)
        bookcls.set_book_genre(name, genre)

    def test_add_new_book_acceptable_name_book_add(
            self, bookcls, valide_book_name
    ):
        "тест: добавление книги с валидным название"
        bookcls.add_new_book(valide_book_name)
        assert valide_book_name in bookcls.get_books_genre()

    def test_add_new_book_name_empty_line_book_dont_add(
            self, bookcls
    ):
        "тест: добавление книги, строка 0 символов"
        book = ''
        bookcls.add_new_book(book)
        assert len(bookcls.get_books_genre()) == 0

    def test_add_new_book_name_41_sumbol_book_dont_add(
            self, bookcls
    ):
        "тест: добавление книги, строка 41 символ"
        book = '12стульев12стульев12стульев12стульев12сту'
        bookcls.add_new_book(book)
        assert len(bookcls.get_books_genre()) == 0

    def test_add_new_book_name_dubbed_earlier_book_dont_add(
            self, bookcls, valide_book_name
    ):
        "тест: добавление дубликата книги"
        bookcls.add_new_book(valide_book_name)
        bookcls.add_new_book(valide_book_name)
        assert len(bookcls.get_books_genre()) == 1

    def test_set_book_genre_book_added_name_genre_in_list_genre_add(
            self, bookcls, valide_book_name
    ):
        "тест: добалвкение жанра к книге, которая ранее добавлена"
        genre = 'Ужасы'
        bookcls.add_new_book(valide_book_name)
        bookcls.set_book_genre(valide_book_name, genre)
        assert bookcls.get_book_genre(valide_book_name) == genre

    def test_set_book_genre_book_not_in_books_genre_dont_add_genre(
            self, bookcls
    ):
        "тест: добавление жанра книги, которой нет в books_genre"
        genre = 'Ужасы'
        book_name = 'test'
        bookcls.set_book_genre(book_name, genre)
        assert bookcls.get_book_genre(book_name) is None

    def test_set_book_genre_add_genre_not_in_genre_list(
            self, bookcls, valide_book_name
    ):
        "тест: добавление несуществующего жанжа, к добавленной ранее книге"
        genre = 'тест'
        bookcls.add_new_book(valide_book_name)
        bookcls.set_book_genre(valide_book_name, genre)
        assert bookcls.get_book_genre(valide_book_name) == ''

    def test_get_book_genre_book_and_genre_added_earlier(
            self, bookcls, valide_book_name, validate_genre
    ):
        """тест: получение жанра книги по названию книги,
        книги и жанр книги добавленны"""
        bookcls.add_new_book(valide_book_name)
        bookcls.set_book_genre(valide_book_name, validate_genre)
        assert bookcls.get_book_genre(valide_book_name) == validate_genre

    def test_get_books_with_specific_genre_an_empty_list_of_books(
            self, bookcls
    ):
        """тест: проверка получения пустого
        списка книг с определенным жанром"""
        genre = bookcls.genre[0]
        check_list = bookcls.get_books_with_specific_genre(genre)
        assert check_list == []

    def test_get_books_with_specific_genre_getting_a_list_of_a_single_item(
            self, bookcls
    ):
        """тест: получение списка книг с определенным жанром.
        Получаем список из 1 элемента"""
        genre_1, genre_2 = bookcls.genre[0], bookcls.genre[1]
        self.add_book_adng_genre(bookcls, 'test_name_1', genre_1)
        self.add_book_adng_genre(bookcls, 'test_name_2', genre_2)

        check_list = bookcls.get_books_with_specific_genre(genre_1)
        assert len(check_list) == 1
        assert 'test_name_1' in check_list

    def test_get_books_with_specific_genre_getting_a_list_of_an_empty_list_with_a_non_existent_genre(
            self, bookcls
    ):
        """тест: получение пустого списка, при несуществующем жанре"""
        genre_1, genre_2 = bookcls.genre[0], bookcls.genre[1]
        self.add_book_adng_genre(bookcls, 'test_name_1', genre_1)
        self.add_book_adng_genre(bookcls, 'test_name_2', genre_2)

        check_list = bookcls.get_books_with_specific_genre('test_genre')

        assert len(check_list) == 0
        assert 'test_name_1' not in check_list
        assert 'test_name_2' not in check_list

    def test_get_books_genre_get_empty_dict(self, bookcls):
        "тест: получение пустого словаря"
        check_dict = bookcls.get_books_genre()

        assert type(check_dict) is dict
        assert len(check_dict) == 0

    def test_get_books_for_children(self, bookcls):
        "тест: проверятся что выводятся книги только для детей"

        """
        Для ревьюера
        понимаю что выполнять assert в цикле for не очень,
        но более простого кода, без содания переменных с перечислением вручную
        всех жанров и потом проврекой их я не придумал.
        Тут проверятся только все что есть в тестируемом классе по жанрам

        Если есть какой то более правильный вариант напишите
        """

        genre_all = bookcls.genre
        genre_all_age_rating = bookcls.genre_age_rating
        # создаем книги по всем жанрам, имена книг это жанр
        for genre in genre_all:
            book_name = genre
            self.add_book_adng_genre(bookcls, book_name, genre)
        # определяем детские жанры
        children_genres = [
            genre for genre in genre_all if genre not in genre_all_age_rating
        ]
        # получаем список детских книг, имена в которы жанр
        children_books = bookcls.get_books_for_children()
        # првоеряем есть ли жанр в списке книг, имена книг это жанр
        for child_genre in children_genres:
            assert child_genre in children_books

    def test_add_book_in_favorites_list(self, bookcls):
        "тест: добавление книги в избранное"
        genre_1 = bookcls.genre[0]
        book_name_1 = 'test_name_1'
        book_name_2 = 'test_name_2'
        self.add_book_adng_genre(bookcls, book_name_1, genre_1)
        self.add_book_adng_genre(bookcls, book_name_2, genre_1)

        bookcls.add_book_in_favorites(book_name_1)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert book_name_1 in favorites_books
        assert len(favorites_books) == 1

    def test_add_book_in_favorites_name_book_not_in_books_genre(self, bookcls):
        "тест: добавление книги в избранное, название книги нет в словаре книг"
        book_name_1 = 'test_name_1'
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 0

        bookcls.add_book_in_favorites(book_name_1)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 0

    def test_add_book_in_favorites_dublicate_book(self, bookcls):
        "тест: добавление в избранно книгу дважды"
        genre_1 = bookcls.genre[0]
        book_name_1 = 'test_name_1'
        self.add_book_adng_genre(bookcls, book_name_1, genre_1)
        bookcls.add_book_in_favorites(book_name_1)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 1

        bookcls.add_book_in_favorites(book_name_1)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 1

    def test_delete_book_from_favorites(self, bookcls):
        "тест: удаление книги из избранного"
        genre_1 = bookcls.genre[0]
        book_name_1 = 'test_name_1'
        book_name_2 = 'test_name_2'
        book_name_3 = 'test_name_3'
        self.add_book_adng_genre(bookcls, book_name_1, genre_1)
        self.add_book_adng_genre(bookcls, book_name_2, genre_1)
        self.add_book_adng_genre(bookcls, book_name_3, genre_1)

        bookcls.add_book_in_favorites(book_name_1)
        bookcls.add_book_in_favorites(book_name_3)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 2

        bookcls.delete_book_from_favorites(book_name_1)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 1
        assert book_name_3 in favorites_books
        assert book_name_2 not in favorites_books
        assert book_name_1 not in favorites_books

    def test_delete_book_from_favorites_name_book_not_in_favorites_list(
            self, bookcls
    ):
        "тест: удаление книги из избранного, название книги нет в избранном"

        genre_1 = bookcls.genre[0]
        book_name_1 = 'test_name_1'
        book_name_2 = 'test_name_2'
        self.add_book_adng_genre(bookcls, book_name_1, genre_1)
        bookcls.add_book_in_favorites(book_name_1)
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 1
        assert book_name_1 in favorites_books
        assert book_name_2 not in favorites_books

        bookcls.delete_book_from_favorites(book_name_2)

        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 1
        assert book_name_1 in favorites_books
        assert book_name_2 not in favorites_books

    def test_get_list_of_favorites_books_get_empty_list(self, bookcls):
        "тест: получаем пустой список избранных книг"
        favorites_books = bookcls.get_list_of_favorites_books()

        assert len(favorites_books) == 0
        assert type(favorites_books) is list
