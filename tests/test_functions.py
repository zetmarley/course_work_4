from src.functions import HeadHunterAPI, Vacancy, JSONSaver
from main import sort_top_vacancies, filter_vacancies, user_interaction
import json

'''Class HeadHunterAPI test'''
def test_get_vacancies():
    hh = HeadHunterAPI()
    vacancies = hh.get_vacancies('Python', 3)
    assert vacancies[:11] == '{"items":[{'
    assert len(json.loads(vacancies)['items']) == 3

'''Class Vacancy test'''
def test_init():
    vacancy = Vacancy('Pavel', 'https://vk.com/id0', 80000, 'Can do everything')
    assert vacancy.__dict__['name'] == 'Pavel'
    assert vacancy.__dict__['url'] == 'https://vk.com/id0'
    assert vacancy.__dict__['salary'] == 80000
    assert vacancy.__dict__['description'] == 'Can do everything'

def test_cast_to_object_list():
    hh = HeadHunterAPI()
    vacancies_list = Vacancy.cast_to_object_list(hh.get_vacancies('Python', 3))
    assert len(vacancies_list) == 3
    for i in vacancies_list:
        assert str(i.__class__) == "<class 'src.functions.Vacancy'>"

'''Class JSONSaver test'''
def show_add_delete_vacancy():
    count = 0
    before = JSONSaver.show()
    vacancy1 = Vacancy('Ivan', 'opa', 'opa', 'amerika evropa')
    vacancy2 = Vacancy('Petya', 'azia', 'evraziya', 'chto za bezobrazie...')
    JSONSaver.add_vacancy(vacancy1)
    JSONSaver.add_vacancy(vacancy2)
    for i in JSONSaver.show():
        if i['description'] == 'amerika evropa' or i['description'] == 'chto za bezobrazie...':
            count += 1
    assert count == 2
    JSONSaver.delete_vacancy(vacancy1)
    JSONSaver.delete_vacancy(vacancy2)
    assert before == JSONSaver.show()

'''Main.py testing'''

def test_sort_top_vacancies():
    hh = HeadHunterAPI()
    sorted_list = sort_top_vacancies(Vacancy.cast_to_object_list(hh.get_vacancies('Python', 3)))
    assert len(sorted_list) == 3
    assert sum(sorted_list[0]['salary'][:-1]) >= sum(sorted_list[1]['salary'][:-1]) >= sum(sorted_list[2]['salary'][:-1])

def test_filter_vacancies():
    vacancies_list = [{'name': 'Vasya', 'url': 'opa cho cho', 'salary': 100000, 'description': 'Menya zvat Petya, i can do everything'},
                      {'name': 'Sanya', 'url': 'opa cho cho', 'salary': 200000, 'description': 'My name is Sanya, i can do everything'},
                      {'name': 'Tolya', 'url': 'opa cho cho', 'salary': 300000, 'description': 'Menya zvat Tolya, i can do everything'}]
    filtered_list = filter_vacancies(vacancies_list, 'Menya zvat')
    assert filtered_list[0]['name'] == 'Vasya'
    assert filtered_list[1]['name'] == 'Tolya'
