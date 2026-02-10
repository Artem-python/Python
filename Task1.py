import doctest


class Smartphone:
    def __init__(self, brand: str, model: str, battery_mah: int, storage_gb: int):
        """
        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_mah: Емкость батареи в mAh
        :param storage_gb: Объем памяти в GB

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3274, 256)
        """
        if not isinstance(brand, str) or not brand:
            raise ValueError("Бренд должен быть непустой строкой")
        if not isinstance(model, str) or not model:
            raise ValueError("Модель должна быть непустой строкой")
        if not isinstance(battery_mah, int) or battery_mah <= 0:
            raise ValueError("Емкость батареи должна быть положительным целым числом")
        if not isinstance(storage_gb, int) or storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным целым числом")

        self.brand = brand
        self.model = model
        self.battery_mah = battery_mah
        self.storage_gb = storage_gb
        self.used_storage = 0
        self.is_on = False

    def turn_on(self) -> bool:
        """
        Включение смартфона
        :return: True если включился, False если уже был включен

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3274, 256)
        >>> phone.turn_on()
        True
        >>> phone.turn_on()  # второй раз
        False
        """
        if self.is_on:
            return False
        self.is_on = True
        return True

    def install_app(self, app_name: str, size_gb: float) -> bool:
        """
        Установка приложения
        :param app_name: Название приложения
        :param size_gb: Размер в GB
        :return: Успешность установки

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3274, 256)
        >>> phone.turn_on()
        True
        >>> phone.install_app("Telegram", 0.85)
        True
        """
        if not self.is_on:
            raise RuntimeError("Смартфон должен быть включен")
        if not isinstance(app_name, str) or not app_name:
            raise ValueError("Название приложения должно быть непустой строкой")
        if not isinstance(size_gb, (int, float)) or size_gb <= 0:
            raise ValueError("Размер должен быть положительным числом")

        if self.used_storage + size_gb > self.storage_gb:
            return False

        self.used_storage += size_gb
        return True


class Student:
    def __init__(self, name: str, student_id: str, course: int):
        """
        :param name: ФИО студента
        :param student_id: Номер студенческого
        :param course: Курс обучения

        Примеры:
        >>> student = Student("Иван Иванов", "Б231-01", 2)
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(student_id, str) or not student_id:
            raise ValueError("Номер студенческого должен быть непустой строкой")
        if not isinstance(course, int) or course < 1 or course > 6:
            raise ValueError("Курс должен быть от 1 до 6")

        self.name = name
        self.student_id = student_id
        self.course = course
        self.grades = {}

    def add_grade(self, subject: str, grade: int) -> bool:
        """
        Добавление оценки
        :param subject: Предмет
        :param grade: Оценка (2-5)
        :return: Успешность добавления

        Примеры:
        >>> student = Student("Иван Иванов", "Б231-01", 2)
        >>> student.add_grade("Математика", 5)
        True
        >>> student.add_grade("Физика", 6)  # недопустимая оценка
        False
        """
        if not isinstance(subject, str) or not subject:
            raise ValueError("Предмет должен быть непустой строкой")
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            return False

        self.grades[subject] = grade
        return True

    def get_average(self) -> float:
        """
        Расчет среднего балла
        :return: Средний балл

        Примеры:
        >>> student = Student("Иван Иванов", "Б231-01", 2)
        >>> student.add_grade("Математика", 5)
        True
        >>> student.add_grade("Физика", 4)
        True
        >>> student.get_average()
        4.5
        """
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        :param title: Название книги
        :param author: Автор
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        """
        if not isinstance(title, str) or not title:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(author, str) or not author:
            raise ValueError("Автор должен быть непустой строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, pages: int) -> int:
        """
        Чтение книги
        :param pages: Сколько страниц прочитать
        :return: Сколько страниц прочитано фактически

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.read(100)
        100
        >>> book.read(2000)  # больше, чем осталось
        1125
        """
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Количество страниц должно быть неотрицательным целым числом")

        pages_left = self.pages - self.current_page
        actual = min(pages, pages_left)
        self.current_page += actual
        return actual

    def get_progress(self) -> float:
        """
        Получение прогресса чтения в %
        :return: Процент прочитанного

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 100)
        >>> book.read(50)
        50
        >>> book.get_progress()
        50.0
        """
        return (self.current_page / self.pages) * 100 if self.pages > 0 else 0.0


if __name__ == "__main__":
    # Запуск доктестов без verbose для чистого вывода
    doctest.testmod()

    print("\n" + "=" * 50)
    print("Демонстрация работы классов:")
    print("=" * 50)

    # Тестирование
    phone = Smartphone("Samsung", "Galaxy S24", 4000, 128)
    phone.turn_on()
    print(f"{phone.brand} {phone.model} включен")

    student = Student("Анна Петрова", "М202-03", 3)
    student.add_grade("Биология", 5)
    student.add_grade("Химия", 4)
    print(f"Средний балл {student.name}: {student.get_average()}")

    book = Book("1984", "Джордж Оруэлл", 328)
    book.read(100)
    print(f"Книга '{book.title}' прочитана на {book.get_progress():.1f}%")





