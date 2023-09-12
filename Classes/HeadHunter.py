import requests
from pprint import pprint

from JobSearchPlatforms import JobSearchPlatforms

# Создаем класс, который наследуется от JobSearchPlatforms
class HeadHunter(JobSearchPlatforms):
    """
    Получает информацию о вакансиях с платформы HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.vacancies = self.get_vacansies()


    def get_vacansies(self, key_word=input('Введите ключевое слово: ')):
        """
        Получает информацию о вакансиях с HeadHunter

        Параметры:
        key_word :  str
            ключевое слово, по которому функция ищет и получает информацию о вакансиях. Вводится пользователем через input

        :return:
        """
        try:
            params = {'text':key_word, 'per_page': 20}
            json_response = requests.get(self.url, params=params).json()
            vacancies_json = json_response['items']
            vacancies_list = []
            for vacancy in vacancies_json:
                vacancies_list.append({'name': vacancy['name'],
                                        'salary': vacancy['salary'],
                                       'responsibility': vacancy['snippet']['responsibility']
                                       'url': vacancy['alternate_url']
                                       })
                pprint(vacancy)
            # pprint(vacancies_list)
        except ConnectionError:
            print('Проверьте подключение к сети')

test = HeadHunter()

test.vacancies
