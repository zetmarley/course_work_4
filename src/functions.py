import json
import requests
from abc import ABC

class HeadHunterAPI(ABC):
    """Класс для работы с HH.ru"""
    """API Ключ не понадобился"""

    url = 'https://api.hh.ru/vacancies'
    response = requests.get(url)

    def init(self):
        self.page = self.response.text

    def get_vacancies(self, search_query, quantity=10):
        """Получаем вакансии"""
        return requests.get(self.url, params={'text' : search_query, 'per_page' : quantity}).text

class Vacancy(HeadHunterAPI):
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

class JSONSaver(HeadHunterAPI):
    """Класс для сохранения вакансий в json файл"""
    def __init__(self):
        pass

    @classmethod
    def show(cls):
        """Показываем содержимое файла"""
        with open('data/vacancies.json', 'r') as file:
            return json.loads(file.read())

    @classmethod
    def add_vacancy(cls, obj):
        """Добавляем вакансию в файл"""
        with open('data/vacancies.json') as fp:
            list_obj = json.load(fp)
            list_obj.append(obj)
        with open('data/vacancies.json', 'w') as json_file:
            json.dump(list_obj, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    @classmethod
    def delete_vacancy(cls, obj):
        """Удаляем вакансию из файла"""
        with open('data/vacancies.json') as fp:
            count = 0
            list_obj = json.load(fp)
            for i in list_obj:
                try:
                    if i['url'] == obj['url']:
                        list_obj.pop(count)
                        count = 0
                    else:
                        count += 1
                except AttributeError:
                    if i['url'] == obj.url:
                        list_obj.pop(count)
                        count = 0
                    else:
                        count += 1

        with open('data/vacancies.json', 'w') as json_file:
            json.dump(list_obj, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)