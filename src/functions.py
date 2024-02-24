import json
import requests
from abc import ABC
class HeadHunterAPI(ABC):
    API_KEY = 'lksjdklasdkl213123'
    url = 'https://api.hh.ru/vacancies'
    response = requests.get(url)

    def init(self):
        self.page = self.response.text

    def get_vacancies(self, search):
        return json.dumps(requests.get(self.url, params={'text':f'{search}'}).text, ensure_ascii=False)

class Vacancy(HeadHunterAPI):
    def __init__(self):
        pass

    @classmethod
    def cast_to_object_list(cls, obj):
        return json.loads(json.loads(obj))['items']

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies('Python')
for i in Vacancy.cast_to_object_list(hh_vacancies):
    print(i)