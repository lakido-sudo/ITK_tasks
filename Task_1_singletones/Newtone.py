class Singleton:
    """

    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'value'):  # Инициализируем только один раз
            self.value = value


# Пример использования
singleton1 = Singleton("Первый экземпляр")
singleton2 = Singleton("Второй экземпляр")

print(singleton1 is singleton2)  # Вывод: True
print(singleton1.value)  # Вывод: Первый экземпляр
