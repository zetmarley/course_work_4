import json

class Vacancy:
    """Класс для работы с вакансиями"""
    count = 1

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    @classmethod
    def cast_to_object_list(self, obj):
        """Форматируем список вакансий в список объектов"""
        box = []
        for i in json.loads(obj)['items']:
            good_salary = []
            try:
                if i['salary']['from'] != None:
                    good_salary.append(i['salary']['from'])
            except:
                good_salary.append(0)

            try:
                if i['salary']['to'] != None:
                    good_salary.append(i['salary']['to'])
            except:
                good_salary.append(0)

            try:
                good_salary.append(i['salary']['currency'])
            except:
                good_salary.append('RUR')
            """Выше убираем None из salary"""
            box.append(Vacancy(i['name'], i['url'], good_salary, i['snippet']['requirement']))
        return box

    @classmethod
    def sort_top_vacancies(cls, vacancies_list):
        """Функция сортирует и составляет топ по зарплате"""
        top_list = []
        for i in vacancies_list: top_list.append(i.__dict__)
        return sorted(top_list, key=lambda d: sum(d['salary'][:-1]), reverse=True)

    @classmethod
    def filter_vacancies(cls, vacancies_list, filter_words):
        """Функция фильтрует вакансии по ключевым словам"""
        temp_list = []
        for b in vacancies_list:
            description = b["description"].translate({ord(','): None})
            description = description.translate({ord('.'): None})
            for a in filter_words.split(' '):
                try:
                    if b in temp_list:
                        continue
                    if a.lower() in description.lower():
                        temp_list.append(b)
                except TypeError:
                    pass
        return temp_list