from src.search_vacancies import Search_Vacancies
import json

'''Class Search_Vacancies test'''
def test_get_vacancies():
    hh = Search_Vacancies()
    vacancies = hh.get_vacancies('Python', 3)
    assert vacancies[:11] == '{"items":[{'
    assert len(json.loads(vacancies)['items']) == 3