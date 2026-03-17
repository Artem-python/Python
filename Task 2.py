BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        """
        Инициализатор класса Book
        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление книги
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает валидную Python строку для создания такого же экземпляра
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Инициализатор класса Library
        :param books: список книг (по умолчанию None - создается пустой список)
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку
        Если книг нет - возвращает 1
        Если книги есть - возвращает id последней книги + 1
        """
        if not self.books:  # если список книг пуст
            return 1
        else:
            # Получаем id последней книги и увеличиваем на 1
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её id
        Если книга не найдена - вызывает ValueError
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        # Если книга не найдена
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1