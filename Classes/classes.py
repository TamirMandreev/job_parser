from abc import ABC, abstractmethod
from pprint import pprint
from operator import itemgetter

import requests

class JobSearchPlatforms(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunter(JobSearchPlatforms):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.vacancies = None


    def get_vacancies(self, keyword=input('Введите ключевое слово: ')):
        try:
            params = {'text': keyword, 'per_page': 100}
            json_response = requests.get(self.url, params=params).json()
            vacancies_json = json_response['items']
            vacancies_list = []
            for vacancy in vacancies_json:
                vacancy_name = vacancy['name']
                vacancy_url = vacancy['alternate_url']
                vacancy_responsibility = vacancy['snippet']['responsibility']

                if vacancy['salary']:

                    vacancy_salaru_from = vacancy["salary"]["from"]
                    vacancy_salaru_to = vacancy["salary"]["to"]
                    vacancy_salaru_currency = vacancy["salary"]["currency"]

                    vacancies_list.append({'name': vacancy_name,
                                           'salary_from': vacancy_salaru_from,
                                           'salary_to': vacancy_salaru_to,
                                           'currencu': vacancy_salaru_currency,
                                           'url': vacancy_url,
                                           'responsibility': vacancy_responsibility})

            self.vacancies = vacancies_list

        except ConnectionError:
            print('Проверьте подключение к сети')

    def salary_sorted_decreasing(self):
        sorted_vacancies = sorted(self.vacancies, key=itemgetter('salary_from'), reverse=True)
        for vacancy in sorted_vacancies:
            print(f"Наименование вакансии: {vacancy['name']}\n"
                  f"Зарплата от {vacancy['salary_from']} до {vacancy['salary_to']}\n"
                  f"Валюта: {vacancy['currencu']}\n"
                  f"URL: {vacancy['url']}\n"
                  f"Краткое описание вакансии: {vacancy['responsibility']}\n")

test = HeadHunter()
test.get_vacancies()
test.salary_sorted_decreasing()



class SuperJob(JobSearchPlatforms):
    secret_key = 'v3.r.131632994.d55f5dd725b34145f36e691951bfbbe8b26b3dc5.52d0aa68c76a90f262dcede8786ea3f10691f5fb'
    id = '2962'

    url = 'https://api.superjob.ru/2.0/vacancies/'



