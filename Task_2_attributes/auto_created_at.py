import datetime


class CreatedAtMeta(type):
    """
    Метакласс, автоматически добавляющий атрибут `created_at` с текущей датой
    и временем к любому классу, который его использует.
    """

    def __new__(cls, name, bases, attrs):
        """
        Вызывается при создании класса.

        Args:
            cls: Ссылка на метакласс.
            name: Имя создаваемого класса.
            bases: Кортеж базовых классов.
            attrs: Словарь атрибутов класса.

        Returns:
            Новый класс с добавленным атрибутом `created_at`.
        """
        attrs['created_at'] = datetime.datetime.now()
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=CreatedAtMeta):
    """
    Пример класса, использующего метакласс `CreatedAtMeta`.

    Атрибуты:
        created_at: Дата и время создания класса (автоматически добавляется
            метаклассом).
    """

    def __init__(self, value):
        """
        Конструктор класса.

        Args:
            value: Произвольное значение для экземпляра класса.
        """
        self.value = value

    def get_value(self):
        """
        Возвращает значение экземпляра класса.

        Returns:
            Значение атрибута `value`.
        """
        return self.value


# Пример использования
instance = MyClass("12345")
print(f"Дата создания класса: {MyClass.created_at}")
print(f"Значение экземпляра: {instance.get_value()}")
