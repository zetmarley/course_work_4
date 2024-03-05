from abc import ABC, abstractmethod
import requests

class HH_API(ABC):
    """Класс для работы с HH.ru"""
    """API Ключ не понадобился"""

    url = 'https://api.hh.ru/vacancies'
    response = requests.get(url)
    page = response.text

    def init(self):
        pass

    @abstractmethod
    def get_vacancies(self, search_query, quantity=10):
        pass