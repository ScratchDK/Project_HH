import requests

from abc import ABC, abstractmethod


class ConnectorAPI(ABC):
    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class ConnectAPIHeadHunter(ConnectorAPI):

    def __init__(self):
        self.__vacancies = {}

    def _connect(self, params=None):
        response = requests.get('https://api.hh.ru/vacancies', params=params)

        if response.status_code == 200:
            print('Подключение к API HeadHunter установлено успешно!\n')
            return response
        else:
            print('Ошибка подключения к API HeadHunter, код ошибки: {}'.format(response.status_code))

    def get_vacancies(self, text: str = None, per_page: str = "1") -> list:
        if text is not None:
            split_text = text.split(", ")
            text = " AND ".join(split_text)

        per_page = int(per_page) if per_page.isdigit() else 1

        if per_page < 0:
            per_page = 1
        elif per_page > 100:
            per_page = 100

        params = {"text": text, "per_page": per_page}
        self.__vacancies = self._connect(params).json()

        return self.__vacancies["items"]
