from src.vacancy import Vacancy
from src.jsonsaver import JSONSaver

'''Class JSONSaver test'''
def test_show_add_delete_vacancy():
    count = 0
    jsonsaver = JSONSaver()
    before = jsonsaver.show()
    vacancy1 = Vacancy('Ivan', 'opa', 'opa', 'amerika evropa')
    vacancy2 = Vacancy('Petya', 'azia', 'evraziya', 'chto za bezobrazie...')
    jsonsaver.add_vacancy(vacancy1.__dict__)
    jsonsaver.add_vacancy(vacancy2.__dict__)
    for i in jsonsaver.show():
        if i['description'] == 'amerika evropa' or i['description'] == 'chto za bezobrazie...':
            count += 1
    assert count == 2
    jsonsaver.delete_vacancy(vacancy1.__dict__)
    jsonsaver.delete_vacancy(vacancy2.__dict__)
    assert before == jsonsaver.show()
