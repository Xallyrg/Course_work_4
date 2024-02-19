from src.HH_API import HeadHunterAPI
from src.Vacancy import Vacancy
from src.FileManager import JSONSaver
from config import PATH_TO_JSON_DATA


"""
Стартуем программу с приветствия и запросов
1) Какие профессии интересуют
2) Ключевые слова (город, требования, обязанности)
3) Минимальная и максимальная зарплата
4) Сколько запросов вывести
"""
print("Добрый день! Давайте подберем вам работу по душе!")
search_query = input("Введите поисковый запрос (какие вакансии вы ищите):  ")
filter_words = input("Введите ключевые слова через запятую (город, требования, обязанности):  ").lower().split(", ")
while True:
    try:
        salary_from = int(input("Введите минимальную желаемую зарплату:  "))
        if salary_from > 0:
            break
        else:
            print("Попробуйте снова, введите положительное число")
            continue
    except ValueError:
        print("Попробуйте снова, введите число")
        continue

while True:
    try:
        salary_to = int(input("Введите максимальную желаемую зарплату:  "))
        if salary_to > salary_from:
            break
        else:
            print(f"Попробуйте снова, введите число большее чем минимальная зарплата {salary_from}")
            continue
    except ValueError:
        print("Попробуйте снова, введите число")
        continue

while True:
    try:
        top_n = int(input("Введите число - топ N вакансий, которые хотите увидеть:  "))
        if top_n > 0:
            break
        else:
            print("Попробуйте снова, введите положительное число")
            continue
    except ValueError:
        print("Попробуйте снова, введите число")
        continue

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies(search_query)

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Отбираем только вакансии, подходящие по кодовым словам
filtered_vacancies = Vacancy.get_filtered_vacancies(vacancies_list, filter_words)

# оставляем только вакансии, подходящие по зарплате
vacancies_by_salary = Vacancy.get_vacancies_by_salary(filtered_vacancies, salary_from, salary_to)

# сортируем вакансии
sorted_vacancies = Vacancy.get_sorted_vacancies(vacancies_by_salary)

# оставляем только верхние top_n вакансий
top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)

# Сохранение информации об интересующих вакансиях в файл
json_saver = JSONSaver()
json_saver.add_to_file(PATH_TO_JSON_DATA, top_vacancies)

# Выводим пользователю то что он просил (я вывожу через метод класса Vacancy потому что так красивее. Записываю в файл в формате JSON
print("Ниже список вакансий, что вы искали")
for vacancy in top_vacancies:
    print(str(vacancy))
# json_saver.read_file(PATH_TO_JSON_DATA)
print("Найденные вакансии сохранены в файл vacancies.json")

# Прощаемся с пользователем
print("Благодарим за использование, надеюсь вы нашли работу мечты!")
