import pytest
from src.Vacancy import Vacancy

vacancy1 = Vacancy("Повар",
                   "Москва",
                   "www.hh.ru/vacancies/123456",
                   "Опыт 10 лет, звание шеф повара",
                   "Любить готовить",
                   10000, 200000)

vacancy2 = Vacancy("Учитель русского",
                   "Балашиха",
                   "www.hh.ru/vacancies/234567",
                   "Опыт не обязательно, ЕГЭ на 80+",
                   "Любить детей",
                   salary_to=50000)

vacancy3 = Vacancy("Уборщик",
                   "Королев",
                   "www.hh.ru/vacancies/456789",
                   "Возраст 30+, опыт в сфере клининга,"
                   "Аккуратность",
                   "Тысяча за час",
                   30000)

vacancy4 = Vacancy("Менеджер ресторана",
                   "Химки",
                   "www.hh.ru/vacancies/567890",
                   "От 3 лет опыта работы в заведении на 30+ работников",
                   "Улаживать конфликты, общаться с клиентами")

vacancy5 = Vacancy("python backend developer",
                   "Москва",
                   "www.hh.ru/vacancy/92292859",
                   "опыт написания кода на django/fast api от 2х лет. опыт работы с микросервисами. умение "
                   "писать юнит-тесты (pytest)",
                   "разработка серверной части. проектирование архитектуры кода, проведение грумминг "
                   "сессий с командой. написание свежего и чистого кода, никакого легаси",
                   120000, 300000)

# Типа список полученный через hh.api
vacancies_from_hh = [
    {
        "name": "python backend developer",
        "area": {"name": "Москва"},
        "alternate_url": "www.hh.ru/vacancy/92292859",
        "salary": {"from": "120000", "to": "300000"},
        "snippet": {"requirement": "опыт написания кода на django", "responsibility": None}
    },
    {
        "name": "Менеджер ресторана",
        "area": {"name": "Химки"},
        "alternate_url": "www.hh.ru/vacancies/567890",
        "salary": {"from": None, "to": None},
        "snippet": {"requirement": "От 3 лет опыта работы в заведении на 30+ работников",
                    "responsibility": "Улаживать конфликты, общаться с клиентами"}
    }
]


@pytest.fixture
def list_of_vacancies():
    list_of_vacancies = [vacancy1, vacancy2, vacancy3, vacancy4, vacancy5]
    return list_of_vacancies


def test_init():
    # слова для фильтрации в основной программе будут приходить в малом регистре
    assert vacancy5.name == "python backend developer"
    assert vacancy5.url == "www.hh.ru/vacancy/92292859"
    assert vacancy5.responsibility == "разработка серверной части. проектирование архитектуры кода, проведение грумминг " \
                                      "сессий с командой. написание свежего и чистого кода, никакого легаси"
    assert vacancy5.salary_to == 300000


def test_repr():
    assert repr(
        vacancy1) == "Vacancy('повар', 'москва', 'www.hh.ru/vacancies/123456', 'опыт 10 лет, звание шеф повара', 'любить готовить', 10000, 200000)"


def test_str():
    assert str(vacancy1) == "Профессия: повар\n" \
                            "Расположение: москва\n" \
                            "Зарплата от 10000 до 200000\n" \
                            "Требования: опыт 10 лет, звание шеф повара\n" \
                            "Обязанности: любить готовить\n" \
                            "Ссылка на сайт hh.ru: www.hh.ru/vacancies/123456\n"


def test_lt():
    assert (vacancy1 < vacancy5) == True
    assert (vacancy5 < vacancy1) == False
    assert (vacancy1 < vacancy1) == False


def test_get_filtered_vacancies(list_of_vacancies):
    assert Vacancy.get_filtered_vacancies(list_of_vacancies, ["повар"]) == [vacancy1]
    assert Vacancy.get_filtered_vacancies(list_of_vacancies, ["опыт"]) == [vacancy1, vacancy2, vacancy3, vacancy4,
                                                                           vacancy5]
    assert Vacancy.get_filtered_vacancies(list_of_vacancies, ["Химки", "python"]) == [vacancy4, vacancy5]
    assert Vacancy.get_filtered_vacancies(list_of_vacancies, ["програмист"]) == []


def test_get_vacancies_by_salary(list_of_vacancies):
    assert Vacancy.get_vacancies_by_salary(list_of_vacancies, 10000, 1000000) == [vacancy1, vacancy2, vacancy3,
                                                                                  vacancy5]
    assert Vacancy.get_vacancies_by_salary(list_of_vacancies, 100000, 500000) == [vacancy5]
    assert Vacancy.get_vacancies_by_salary(list_of_vacancies, 100000, 200000) == []


def test_get_sorted_vacancies(list_of_vacancies):
    assert Vacancy.get_sorted_vacancies(list_of_vacancies) == [vacancy5, vacancy3, vacancy1, vacancy2, vacancy4]


def test_get_top_vacancies(list_of_vacancies):
    assert Vacancy.get_top_vacancies(Vacancy.get_sorted_vacancies(list_of_vacancies), 2) == [vacancy5, vacancy3]
    assert Vacancy.get_top_vacancies(list_of_vacancies, 4) == [vacancy1, vacancy2, vacancy3, vacancy4]


def test_cast_to_object_list():
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[0].name == 'python backend developer'
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[1].city == 'химки'
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[0].url == 'www.hh.ru/vacancy/92292859'
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[
               1].requirement == 'от 3 лет опыта работы в заведении на 30+ работников'
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[0].responsibility == 'не указано'
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[1].salary_from == 0
    assert Vacancy.cast_to_object_list(vacancies_from_hh)[0].salary_to == 300000
