import pytest

from bookcollector import BooksCollector


@pytest.fixture(scope='function')
def bookcls():
    bookcls = BooksCollector()
    return bookcls


@pytest.fixture
def valide_book_name():
    return '12 стульев'


@pytest.fixture
def validate_genre():
    return 'Ужасы'
