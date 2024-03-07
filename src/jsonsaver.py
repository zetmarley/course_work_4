import json
from abc import ABC, abstractmethod
class JSONAbstract(ABC):
    """Абстрактный класс для JSONSaver"""
    def __init__(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add_vacancy(self, obj):
        pass

    @abstractmethod
    def delete_vacancy(self, obj):
        pass

class JSONSaver(JSONAbstract):
    """Класс для сохранения вакансий в json файл"""
    def __init__(self):
        pass

    def show(self):
        """Показываем содержимое файла"""
        with open('data/vacancies.json', 'r') as file:
            return json.loads(file.read())

    def add_vacancy(self, obj):
        """Добавляем вакансию в файл"""
        with open('data/vacancies.json') as fp:
            list_obj = json.load(fp)
            list_obj.append(obj)
        with open('data/vacancies.json', 'w') as json_file:
            json.dump(list_obj, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    def delete_vacancy(self, obj):
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
