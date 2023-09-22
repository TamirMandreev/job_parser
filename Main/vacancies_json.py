from abc import ABC
from Vacancy import Vacancy
import json

# Создаем абстрактный класс для работы с json форматом
class working_json_file(ABC):
    """
    Абстрактный класс. Устанавливает обязательные для реализации в дочерних классах функции
    """
    def json_dump(self):
        """
        Загружает список вакансий в json файл
        :return:
        """
        pass

    def json_load(self):
        """
        Скачивает список вакансий из json файла
        """
        pass

    def json_delete(self):
        """
        Удаляет вакансии из json файла
        :return:
        """
        pass


class Json_dump:
    """
    Класс для загрузки списка вакансий в json файл
    """

    @classmethod
    def json_dump(self):
        """
        Загружает список вакансий в json файл vacancies.json
        """
        with open('/home/tamir/PycharmProjects/job_parser/vacancies.json', 'a') as json_file:
            json.dump(Vacancy.vacancies_list_of_dictionaries, json_file)
        print('Вакансии успешно добавлены в JSON файл')

