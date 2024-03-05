from src.vacancy import Vacancy
from src.jsonsaver import JSONSaver

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
