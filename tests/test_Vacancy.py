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




