from Vacancy import Vacancy
from vacancies_json import Json_dump

print("""Где искать вакансии?
1. HeadHunter
2. SuperJob
3. На обеих платформах
""")

user_answer_1 = input('Введите цифру: ')

if user_answer_1 == '1':
    Vacancy.initialization_HH()
elif user_answer_1 == '2':
    Vacancy.initialization_SJ()
elif user_answer_1 == '3':
    Vacancy.initialization_HH()
    Vacancy.initialization_SJ()

print('''Отсортировать вакансии по заработной плате?
1. Да
2. Нет''')
user_answer_2 = input("Введите цифру")

while True:
    if user_answer_2 == '1':
        Vacancy.sorted_vacancies()
        Vacancy.print_vacancies()
        break
    elif user_answer_2 == '2':
        Vacancy.print_vacancies()
        break
    else:
        print('Неправильный ответ. Введите повторно.')
        user_answer_2 = input()

print('''Хотите загрузить данные в json файл?
1. Да
2. Нет''')
user_answer_3 =  input("Введите цифру")
while True:
    if user_answer_2 == '1':
        Json_dump.json_dump()
        break
    elif user_answer_2 == '2':
        print('Программа закончена')
        break
    else:
        print('Неправильный ответ. Программа закончена')
