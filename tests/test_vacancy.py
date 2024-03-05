from src.vacancy import Vacancy
from src.search_vacancies import Search_Vacancies

'''Class Vacancy test'''

def test_init():
    vacancy = Vacancy('Pavel', 'https://vk.com/id0', 80000, 'Can do everything')
    assert vacancy.__dict__['name'] == 'Pavel'
    assert vacancy.__dict__['url'] == 'https://vk.com/id0'
    assert vacancy.__dict__['salary'] == 80000
    assert vacancy.__dict__['description'] == 'Can do everything'

def test_cast_to_object_list():
    hh = Search_Vacancies()
    vacancies_list = Vacancy.cast_to_object_list(hh.get_vacancies('Python', 3))
    assert len(vacancies_list) == 3
    for i in vacancies_list:
        assert str(i.__class__) == "<class 'src.vacancy.Vacancy'>"

def test_sort_top_vacancies():
    hh = Search_Vacancies()
    sorted_list = Vacancy.sort_top_vacancies(Vacancy.cast_to_object_list(hh.get_vacancies('Python', 3)))
    assert len(sorted_list) == 3
    assert sum(sorted_list[0]['salary'][:-1]) >= sum(sorted_list[1]['salary'][:-1]) >= sum(sorted_list[2]['salary'][:-1])

def test_filter_vacancies():
    vacancies_list = [{'name': 'Vasya', 'url': 'opa cho cho', 'salary': 100000, 'description': 'Menya zvat Petya, i can do everything'},
                      {'name': 'Sanya', 'url': 'opa cho cho', 'salary': 200000, 'description': 'My name is Sanya, i can do everything'},
                      {'name': 'Tolya', 'url': 'opa cho cho', 'salary': 300000, 'description': 'Menya zvat Tolya, i can do everything'}]
    filtered_list = Vacancy.filter_vacancies(vacancies_list, 'Menya zvat')
    assert filtered_list[0]['name'] == 'Vasya'
    assert filtered_list[1]['name'] == 'Tolya'