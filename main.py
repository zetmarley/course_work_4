from src.functions import HeadHunterAPI, Vacancy, JSONSaver

"""Этим файлом будет пользоваться юзер"""

def user_menu():
    print('Привет!', end=' ')
    while True:
        choice = int(input('\nВыбери что нужно:\n1. Поиск вакансий\n'
          '2. Посмотреть и отредактировать сохраненные вакансии\n'
          '3. Выйти\nОтвет: '))
        if choice == 1:
            user_search()
        elif choice == 2:
            user_vacancies_list()
        elif choice == 3:
            break
        else:
            print("Неправильный ответ.")

def user_search():
    """Сама функция для использования"""
    hh = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = hh.get_vacancies(search_query, top_n)
    vacancies_list = Vacancy.cast_to_object_list(vacancies)
    sorted_top_vacancies = Vacancy.sort_top_vacancies(vacancies_list)
    for i in sorted_top_vacancies:
        print(f'\nВакансия: {i["name"]}\nURL: {i["url"]}\nЗарплата: {" ".join([str(x) for x in i["salary"]])}\nОписание: {i["description"]}')
    filter_words = input("\nВведите ключевые слова для фильтрации вакансий: ")
    filtered_vacancies = Vacancy.filter_vacancies(sorted_top_vacancies, filter_words)
    for i in filtered_vacancies:
        print(f'\nВакансия: {i["name"]}\nURL: {i["url"]}\nЗарплата: {" ".join([str(x) for x in i["salary"]])}\nОписание: {i["description"]}')
    if input("\nСохранить отфильтрованные вакансии? (y/n): ") == 'y':
        for i in filtered_vacancies:
            JSONSaver.add_vacancy(i)

def user_vacancies_list():
    dict_vacancies = {}
    count = 1
    print('Сохраненные вакансии :')
    for i in JSONSaver.show():
        dict_vacancies[f'{count}'] = i
        print(f'\nВакансия {count}: {i["name"]}\nURL: {i["url"]}\nЗарплата: {" ".join([str(x) for x in i["salary"]])}\nОписание: {i["description"]}')
        count += 1
    choice = int(input('\n1. Добавить вакансию вручную.\n2. Удалить вакансию.\n3. Выйти в меню\nОтвет: '))
    if choice == 1:
        vacancy = Vacancy(input("Введи название вакансии: "), input("Введи ссылку на вакансию: "), input('Введи заработную плату: '), input("Введи описание вакансии: "))
        JSONSaver.add_vacancy(vacancy.__dict__)
        dict_vacancies[f'{count}'] = vacancy.__dict__
        print("Вакансия добавлена!")
    elif choice == 2:
        delete_choice = input('Номер какой вакансии вы желаете удалить?\nОтвет: ')
        for k, v in dict_vacancies.items():
            if k == str(delete_choice):
                JSONSaver.delete_vacancy(v)
                print("Вакансия удалена!")
            elif int(delete_choice) > int(k):
                delete_choice = input('Неправильный номер вакансии!\nНомер какой вакансии вы желаете удалить?\nОтвет: ')

if __name__ == "__main__":
    user_menu()