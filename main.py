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
    for a in filter_words:
        for b in vacancies_list:
            try:
                if a in b['description']:
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
    for i in sorted_top_vacancies: print(i)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(sort_top_vacancies(vacancies_list), filter_words)
    for i in filtered_vacancies: print(i)

if __name__ == "__main__":
    user_interaction()

