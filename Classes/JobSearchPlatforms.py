from abc import ABC, abstractmethod

# Создаем абстрактный класс "Платформы для поиска работы", от которого будут наследоваться классы для работы с конкретными платформами.
class JobSearchPlatforms(ABC):
    """
    Абстрактный класс. Устанавливает обязательные для реализации в дочерних классах функции
    """

    @abstractmethod
    def get_vacansies(self, key_word):
        """
        Получает информацию о вакансиях, размещенных на платформах для поиска работы

        Параметры:
        key_word : str
            ключевое слово, по которому функция ищет и получает информацию о вакансиях
        """
        pass
