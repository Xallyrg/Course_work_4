from src.HH_API import HeadHunterAPI


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


vac1 = Vacancy("Парикмахер", "Москва", "https://hh.ru/vacancy/92918782",
               "ОТ ВАС: Опыт работы от 1 года. Умение выполнять мужские, женские, детские стрижки, окрашивания любой сложности, уходовые процедуры.",
               "РАБОТАЕМ НА МАТЕРИАЛАХ:", 1, 10)
vac2 = Vacancy("Прогер", "Москва", "https://hh.ru",
               "ОТ ВАС: Опыт работы от 100 лет.", "Ответсвенность", 1, 100)
# print(repr(vac))
# print(str(vac1))
# print(str(vac2))

print(vac1 < vac2)
print(vac1 < vac1)
print(vac2 < vac1)

# hh_api = HeadHunterAPI()
# hh_response = hh_api.get_vacancies("парикмахер")
# for vacancy in hh_response:
#     print(vacancy)
