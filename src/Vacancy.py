# from src.HH_API import HeadHunterAPI


class Vacancy:
    """
    класс для вакансии
    Содержит следующие атрибуты:
    Наименование вакансии
    Город
    Ссылка на вакансию
    Требования
    Обязанности
    Зарплата от
    Зарплата до
    """

    def __init__(self, name: str, city: str, url: str, requirement: str, responsibility: str, salary_from: int = 0,
                 salary_to: int = 0):
        self.name = name.lower()
        self.city = city.lower()
        self.url = url.lower()
        self.requirement = requirement.lower()
        self.responsibility = responsibility.lower()
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        """
        Вызвращает строку инициализации класса
        :return:
        """
        return (f"{self.__class__.__name__}"
                f"({self.name}, "
                f"{self.city}, "
                f"{self.url}, "
                f"{self.requirement}, "
                f"{self.responsibility}, "
                f"{self.salary_from}, "
                f"{self.salary_to})")

    def __str__(self):
        """
        Выводим в удобном для восприятия виде. Сначала более важные параметры
        :return:
        """
        if self.salary_from == 0 and self.salary_to == 0:
            return (f"Профессия: {self.name}\n"
                    f"Расположение: {self.city}\n"
                    f"Зарплата не указана\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n"
                    f"Ссылка на сайт hh.ru: {self.url}\n")
        elif self.salary_from == 0:
            return (f"Профессия: {self.name}\n"
                    f"Расположение: {self.city}\n"
                    f"Зарплата до {self.salary_to}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n"
                    f"Ссылка на сайт hh.ru: {self.url}\n")
        elif self.salary_to == 0:
            return (f"Профессия: {self.name}\n"
                    f"Расположение: {self.city}\n"
                    f"Зарплата от {self.salary_from}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n"
                    f"Ссылка на сайт hh.ru: {self.url}\n")
        else:
            return (f"Профессия: {self.name}\n"
                    f"Расположение: {self.city}\n"
                    f"Зарплата от {self.salary_from} до {self.salary_to}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n"
                    f"Ссылка на сайт hh.ru: {self.url}\n")

    def __lt__(self, other):
        """
        Метод чтобы проверить, что "первая вакансия" < "второй" по зарплате
        В начале проверяем, что сравнивать можно только две вакансии

        Сравниваем сначала по нижнему порогу. Если по нему не получилось, то по верхнему

        Если в обеих вакансиях есть только нижний или только верхний порог, то сравниваем по нему
        Если в одной есть нижний порог, а в другой нет, то та где есть побеждает
        Если есть оба, то сравниваем по нижнему
        :param other:
        :return:
        """
        if isinstance(other, Vacancy):
            # Сравниваем нижние границым в одну сторону
            if self.salary_from < other.salary_from:
                return True
            # в другую сторону
            elif self.salary_from > other.salary_from:
                return False
            # теперь нижние равны (возможно нулю) и сравниваем верхние границы
            elif self.salary_to < other.salary_to:
                return True
            # остался случай когда и верхние равны, или когда у other верхняя ЗП больше
            else:
                return False
        else:
            raise ValueError('Сравнивать можно только две вакансии.')

    @staticmethod
    def get_filtered_vacancies(vacancies_list: list, filter_word: list) -> list:
        """
        Оставляет от списка вакансий только те, в которых встречаются ключевые слова
        (если хотя бы одно ключевое слово есть в названии, городе, требованиях или обязанностях то ОК)
        """
        filtered_vacancies = []
        for vacancy in vacancies_list:
            for word in filter_word:
                if (word.lower() in vacancy.name or
                        word.lower() in vacancy.city or
                        word.lower() in vacancy.requirement or
                        word.lower() in vacancy.responsibility):
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies

    @staticmethod
    def get_vacancies_by_salary(vacancies_list: list, salary_from: int, salary_to: int):
        """
        Оставляет от списка вакансий только те, что подходят под диапозон зарплаты\
        """
        vacancies_by_salary = []
        for vacancy in vacancies_list:
            # Если обе границы попали
            if (salary_from <= vacancy.salary_from <= salary_to and
                  salary_from <= vacancy.salary_to <= salary_to):
                vacancies_by_salary.append(vacancy)
            # Если у вакансии нет нижней границы, но верхняя попала
            elif vacancy.salary_from == 0 and salary_from <= vacancy.salary_to <= salary_to:
                vacancies_by_salary.append(vacancy)
            # Если у вакансии нет верхней границы, но нижняя попала
            elif vacancy.salary_to == 0 and salary_from <= vacancy.salary_from <= salary_to:
                vacancies_by_salary.append(vacancy)
        return vacancies_by_salary

    @staticmethod
    def get_sorted_vacancies(unsorted_vacancies: list) -> list:
        """
        Сортирует список вакансий по уменьшению зарплаты
        """
        sorted_vacancies = sorted(unsorted_vacancies, reverse=True)
        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(vacancies_list: list, top_number: int) -> list:
        """
        Формирует список из первых N позиций
        (у нас это будет топ по зарплате, потому что будем применять после get_sorted_vacancies)
        """
        return vacancies_list[0:top_number]

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list) -> list:
        """
        Создает список объектов-вакансий из данных, полученных через api.hh.ru
        """
        vacancies_list = []
        for vacancy in hh_vacancies:

            name = vacancy["name"].lower()

            city = vacancy["area"]["name"].lower()

            url = vacancy["alternate_url"].lower()

            try:
                salary_from = int(vacancy["salary"]["from"])
            except TypeError:
                salary_from = 0

            try:
                salary_to = int(vacancy["salary"]["to"])
            except TypeError:
                salary_to = 0

            requirement = vacancy["snippet"]["requirement"]
            if requirement is None:
                requirement = "не указано"
            else:
                requirement = requirement.lower()

            responsibility = vacancy["snippet"]["responsibility"]
            if responsibility is None:
                responsibility = "не указано"
            else:
                responsibility = responsibility.lower()

            current_vacancy = cls(name, city, url, requirement, responsibility, salary_from, salary_to)
            vacancies_list.append(current_vacancy)
        return vacancies_list


# vac1 = Vacancy("Парикмахер", "Москва", "https://hh.ru/vacancy/92918782",
#                "ОТ ВАС: Опыт работы от 1 года. Умение выполнять мужские, женские, детские стрижки, окрашивания любой сложности, уходовые процедуры.",
#                "РАБОТАЕМ НА МАТЕРИАЛАХ:", 2, 10)
# vac2 = Vacancy("Прогер", "Москва", "https://hh.ru",
#                "ОТ ВАС: Опыт работы от 100 лет.", "Ответсвенность", 1, 100)
# print(repr(vac))
# print(str(vac1))
# print(str(vac2))

# print(vac1 < vac2)
# print(vac1 < vac1)
# print(vac2 < vac1)

# list_of_vac = [vac1,vac2]

# vac = Vacancy.get_filtered_vacancies(list_of_vac, ['прог'])
# for vacation in vac:
#     print(str(vacation))

# vac = Vacancy.get_vacancies_by_salary(list_of_vac, 2,510)
# for vacation in vac:
#     print(str(vacation))

# vac = Vacancy.get_sorted_vacancies(list_of_vac)
# vac = Vacancy.get_top_vacancies(vac, 1)
# for vacation in vac:
#     print(str(vacation))

# hh_api = HeadHunterAPI()
# hh_response = hh_api.get_vacancies("python")
# list_of_vacancies = Vacancy.cast_to_object_list(hh_response)
# list_of_vacancies = Vacancy.get_filtered_vacancies(list_of_vacancies, ['Москва'])
# list_of_vacancies = Vacancy.get_vacancies_by_salary(list_of_vacancies, 150000, 100000000)
# list_of_vacancies = Vacancy.get_sorted_vacancies(list_of_vacancies)
# list_of_vacancies = Vacancy.get_top_vacancies(list_of_vacancies, 3)
#
# for vacancy in list_of_vacancies:
#      print(str(vacancy))
#
# print(len(list_of_vacancies))
