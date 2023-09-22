import requests
from pprint import pprint


class SuperJob:
    """
    Получает информацию о вакансиях с платформы HeadHunter
    """

    @classmethod
    def get_vacancies(cls, key_word = None):
        """
        Получает информацию о вакансиях с SuperJob

        Параметры:
        key_word :  str
            ключевое слово, по которому функция ищет и получает информацию о вакансиях. Вводится пользователем через input

        Возвращает:
        vacancies_list : list
            список словарей. В каждом словаре содержится name, salary_from, salary_to, responsibility, url отдельно взятой вакансии.
        """


        try:
            key_word = input('Введите ключевое слово для поиска ваканский на SuperJob: ')
            url = 'https://api.superjob.ru/2.0/vacancies/'
            HEADERS = {'X-Api-App-Id': 'v3.r.131632994.d55f5dd725b34145f36e691951bfbbe8b26b3dc5.52d0aa68c76a90f262dcede8786ea3f10691f5fb'}
            params = {'keyword': key_word}
            response = requests.get(url, headers=HEADERS, params=params).json()
            vacancies_json = response['objects']
            vacancies_list = []
            for vacancy in vacancies_json:
                vacancies_list.append({
                    'name': vacancy['profession'],
                    'responsibility': vacancy['candidat'],
                    'salary_to': vacancy['payment_from'],
                    'salary_from': vacancy['payment_to'],
                    'currency': vacancy['currency'],
                    'url': vacancy['link']
                })
            return vacancies_list
        except ConnectionError:
            print('Проверьте подключение к сети')


