from src.hh_api import HH_API
import requests

class Search_Vacancies(HH_API):
    """Класс для поиска вакансий"""
    def init(self):
        pass

    def get_vacancies(self, search_query, quantity=10):
        """Получаем вакансии"""
        return requests.get(self.url, params={'text': search_query, 'per_page': quantity}).text