from HeadHunter import HeadHunter
from SuperJob import SuperJob
import json
from pprint import pprint

class Vacancy:
    """
    Класс для работы с вакансиями
    """
    # Создаем пустой список, куда будем добавлять вакансии с HeadHunter и SuperJob
    vacancies = []

    # Создаем пустой список, в который будем добавлять вакансии с HeadHunter и SuperJob для их дампа в json файл
    vacancies_list_of_dictionaries = []

    def __init__(self, name, salary_from, salary_to, salary_currency, responsibility, url):
        """
        Устанавливает все необходимые атрибуты для объекта Vacancy

        Параметры
        name : str
            Наименование вакансии
        salary_from : int
            Нижний порог зарплаты
        salary_to : int
            Верхний порог зарплаты
        salary_currency : str
            Валюта зарплаты
        responsibility : str
            Краткое описание вакансии
        url : str
            Ссылка на вакансию
        """
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.responsibility = responsibility
        self.url = url

    def __str__(self):
        """
        Возвращает описание атрибутов экземпляра класса для обычного пользователя
        :return:
        """
        return (f'Наименование вакансии: {self.name}\n'
                f'Зарплата от {self.salary_from} до {self.salary_to} {self.salary_currency}\n'
                f'Требования: {self.responsibility}\n'
                f'url: {self.url}\n')

    @classmethod
    def initialization_HH(self):
        """
        Создает (инициализирует) экземпляры класса (вакансии) с помощью информации с HeadHunter
        Добавляет в переменную класса vacancies наименование вакансии, уровень зарплаты,
        краткое описание требований и ссылку на вакансию
        """
        for item in HeadHunter.get_vacansies():
            name = item['name']
            # Без условия обращение из цикла к item['salary']['from'] вызывает ошибку
            if item['salary'] is not None and 'from' in item['salary'] and item['salary']['from'] is not None:
                salary_from = item['salary']['from']
            else:
                salary_from = 0
            if item['salary'] is not None:
                salary_to = item['salary']['to']
            else:
                salary_to = '~'
            if item['salary'] is not None:
                salary_currencu = item['salary']['currency']
            responsibility = item['responsibility']
            url = item['url']
            vacancy = Vacancy(name, salary_from, salary_to, salary_currencu, responsibility, url)
            Vacancy.vacancies.append(vacancy)
            vacancy_dict = {'name': name, 'salary_from': salary_from, 'salary_to': salary_to,
                            'salary_currencu': salary_currencu, 'responsibility': responsibility, 'url': url}
            Vacancy.vacancies_list_of_dictionaries.append(vacancy_dict)

    @classmethod
    def initialization_SJ(self):
        """
        Создает (инициализирует) экземпляры класса (вакансии) с помощью информации с SuperJob
        Добавляет в переменную класса vacancies наименование вакансии, уровень зарплаты,
        описание требований и ссылку на вакансию

        """
        for item in SuperJob.get_vacancies():
            name = item['name']
            salary_from = item['salary_from']
            salary_to = item['salary_to']
            salary_currencu = item['currency']
            responsibility = item['responsibility']
            url = item['url']
            vacancy = Vacancy(name, salary_from, salary_to, salary_currencu, responsibility, url)
            Vacancy.vacancies.append(vacancy)
            vacancy_dict = {'name': name, 'salary_from': salary_from, 'salary_to': salary_to, 'salary_currencu': salary_currencu, 'responsibility': responsibility, 'url': url}
            Vacancy.vacancies_list_of_dictionaries.append(vacancy_dict)


    @classmethod
    def print_vacancies(self):
        """
        Выводит описание экземпляров класс (вакансий)
        """
        for vacancy in Vacancy.vacancies:
            print(str(vacancy))

    @classmethod
    def sorted_vacancies(self):
        """
        Сортирует список вакансий по зарплате от большей к меньшей
        :return:
        """
        sorted_vacancies = sorted(Vacancy.vacancies, key=lambda x: x.salary_from)
        for i in sorted_vacancies:
            print(str(i))


        




