from src.functions import HeadHunterAPI, Vacancy

"""Этим файлом будет пользоваться юзер"""

def sort_top_vacancies(vacancies_list):
    """Функция сортирует и составляет топ по зарплате"""
    top_list = []
    for i in vacancies_list: top_list.append(i.__dict__)
    return sorted(top_list, key=lambda d: sum(d['salary'][:-1]), reverse=True)

def filter_vacancies(vacancies_list, filter_words):
    """Функция фильтрует вакансии по ключевым словам"""
    temp_list = []
    for b in vacancies_list:
        description = b["description"].translate({ord(','): None})
        description = description.translate({ord('.'): None})
        for a in filter_words.split(' '):
            try:
                if b in temp_list:
                    continue
                if a in description:
                    temp_list.append(b)
            except TypeError:
                pass
    return temp_list

def user_interaction():
    """Сама функция для использования"""
    hh = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = hh.get_vacancies(search_query, top_n)
    vacancies_list = Vacancy.cast_to_object_list(vacancies)
    sorted_top_vacancies = sort_top_vacancies(vacancies_list)
    for i in sorted_top_vacancies:
        print(f'\nВакансия: {i["name"]}\nURL: {i["url"]}\nЗарплата: {" ".join([str(x) for x in i["salary"]])}\nОписание: {i["description"]}')
    filter_words = input("\nВведите ключевые слова для фильтрации вакансий: ")
    filtered_vacancies = filter_vacancies(sorted_top_vacancies, filter_words)
    for i in filtered_vacancies:
        print(f'\nВакансия: {i["name"]}\nURL: {i["url"]}\nЗарплата: {" ".join([str(x) for x in i["salary"]])}\nОписание: {i["description"]}')

if __name__ == "__main__":
    user_interaction()