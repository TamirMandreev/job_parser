import requests
from pprint import pprint

from JobSearchPlatforms import JobSearchPlatforms


# Создаем класс, который наследуется от JobSearchPlatforms
class HeadHunter(JobSearchPlatforms):
    """
    Получает информацию о вакансиях с платформы HeadHunter
    """

    @classmethod
    def get_vacansies(cls, key_word=None):
        """
        Получает информацию о вакансиях с HeadHunter

        Параметры:
        key_word :  str
            ключевое слово, по которому функция ищет и получает информацию о вакансиях. Вводится пользователем через input

        Возвращает:
        vacancies_list : list
            список словарей. В каждом словаре содержится name, salary, responsibility, url отдельно взятой вакансии.
        """
        try:
            key_word = input('Введите ключевое слово для поиска вакансий на HeadHunter: ')
            params = {'text': key_word, 'per_page': 20}
            url = 'https://api.hh.ru/vacancies'
            json_response = requests.get(url, params=params).json()
            vacancies_json = json_response['items']
            vacancies_list = []
            for vacancy in vacancies_json:
                vacancies_list.append({'name': vacancy['name'],
                                       'responsibility': vacancy['snippet']['responsibility'],
                                       'salary': vacancy['salary'],
                                       'url': vacancy['alternate_url']
                                       })

            return vacancies_list

        except ConnectionError:
            print('Проверьте подключение к сети')

