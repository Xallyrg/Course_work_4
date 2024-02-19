

class Vacancy:
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
        return (f"{self.__class__.__name__}"
                f"({self.name}, "
                f"{self.city}, "
                f"{self.url}, "
                f"{self.requirement}, "
                f"{self.responsibility}, "
                f"{self.salary_from}, "
                f"{self.salary_to})")

    def __str__(self):
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


vac = Vacancy("Парикмахер", "Москва", "https://hh.ru/vacancy/92918782",
              "ОТ ВАС: Опыт работы от 1 года. Умение выполнять мужские, женские, детские стрижки, окрашивания любой сложности, уходовые процедуры.",
              "РАБОТАЕМ НА МАТЕРИАЛАХ:", "80000", "160000")
# print(repr(vac))
print(str(vac))

