# Тесты
___
Создан класс TestBooksCollector в котом хранятся и запускаются тесты для прорвеки класса BooksCollector
Создан файл conftest в котором находятся фикстуры pytest

1. test_add_new_book_acceptable_name_book_add - тест: добавление книги с валидным название
2. test_add_new_book_name_empty_line_book_dont_add - тест: добавление книги, строка 0 символов
3. test_add_new_book_name_41_sumbol_book_dont_add - тест: добавление книги, строка 41 символ
4. test_add_new_book_name_dubbed_earlier_book_dont_add - тест: добавление дубликата книги
5. test_set_book_genre_book_added_name_genre_in_list_genre_add - тест: добалвкение жанра к книге, которая ранее добавлена
6. test_set_book_genre_book_not_in_books_genre_dont_add_genre - тест: добавление жанра книги, которой нет в books_genre
7. test_set_book_genre_add_genre_not_in_genre_list - тест: добавление несуществующего жанжа, к добавленной ранее книге
8. test_get_book_genre_book_and_genre_added_earlier - тест: получение жанра книги по названию книги, книги и жанр книги добавленны
9. test_get_books_with_specific_genre_an_empty_list_of_books - тест: проверка получения пустого списка книг с определенным жанром
10. test_get_books_with_specific_genre_getting_a_list_of_a_single_item - тест: получение списка книг с определенным жанром. Получаем список из 1 элемента.
11. test_get_books_with_specific_genre_getting_a_list_of_an_empty_list_with_a_non_existent_genre - тест: получение пустого списка, при несуществующем жанре
12. test_get_books_genre_get_empty_dict - тест: получение пустого словаря
13. test_get_books_for_children - тест: проверятся что выводятся книги только для детей
14. test_add_book_in_favorites_list - тест: добавление книги в избранное
15. test_add_book_in_favorites_name_book_not_in_books_genre - тест: добавление книги в избранное, название книги нет в словаре книг
16. test_add_book_in_favorites_dublicate_book - тест: добавление в избранно книгу дважды
17. test_delete_book_from_favorites - тест: удаление книги из избранного
18. test_delete_book_from_favorites_name_book_not_in_favorites_list - тест: удаление книги из избранного, название книги нет в избранном
19. test_get_list_of_favorites_books_get_empty_list - тест: получаем пустой список избранных книг