import json

class JSONSaver:
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