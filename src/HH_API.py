import json
from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    """
    абстрактный класс для работы с API сервиса с вакансиями
    """
    @abstractmethod
    def get_vacancies(self, vacancy_name):
        pass


class HeadHunterAPI(BaseAPI):
    """
    класс, наследующийся от абстрактного класса, для работы с платформой hh.ru
    :param BaseAPI:
    :return:
    """
    def get_vacancies(self, vacancy_name):
        params = {
            "text": f"NAME:{vacancy_name}",
            "page": 0,
            "per_page": 100
        }
        response = requests.get(f"https://api.hh.ru/vacancies/", params=params)
        hh_data = json.loads(response.text)
        hh_vacancies = hh_data["items"]
        return hh_vacancies


# hh_api = HeadHunterAPI()
# hh_response = hh_api.get_vacancies("парикмахер")
# print(hh_response)
# for vacancy in hh_response:
#     print(vacancy)
