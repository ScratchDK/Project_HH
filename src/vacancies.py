class Vacancy:
    __slots__ = ['id', 'name', 'address', 'salary_from', 'salary_to', 'requirement',
                 'responsibility', 'vacancy', 'list_vacancies', 'url']

    def __init__(self, data: dict, list_data: list = None):

        self.list_vacancies = list_data if list_data is not None else []

        if self.__validate_data(data):
            self.id = data.get("id")
            self.name = data.get("name", "не указано")
            self.address = data["address"].get("raw") if data.get("address") else "не указан"
            self.salary_from = self.__validate_salary_from(data)
            self.salary_to = self.__validate_salary_to(data)
            self.requirement = data["snippet"]["requirement"] if data["snippet"].get("requirement") else "не указаны"
            self.responsibility = data["snippet"]["responsibility"]\
                if data["snippet"].get("responsibility") else "не указаны"
            self.url = data["alternate_url"]

            self.vacancy_to_dict()

    def vacancy_to_dict(self):
        new_dict = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "url": self.url
        }
        self.list_vacancies.append(new_dict)

    def __str__(self):
        if self.salary_from == 0:
            self.salary_from = "не указана"

        if self.salary_to == 0:
            self.salary_to = "не указана"

        return (f"{self.name.upper()}\n"
                f"Зарплата: от {self.salary_from} - до {self.salary_to}\n"
                f"Адрес: {self.address}\n"
                f"Требования: {self.requirement}\n"
                f"Обязаности: {self.responsibility}\n"
                f"Ссылка: {self.url}\n")

    @staticmethod
    def __validate_data(data):
        if not isinstance(data, dict):
            return False
        if "snippet" not in data or "address" not in data or "salary" not in data:
            return False
        return True

    @staticmethod
    def __validate_salary_from(data):
        result = data["salary"].get("from") if data.get("salary") else 0
        return result if result is not None else 0

    @staticmethod
    def __validate_salary_to(data):
        result = data["salary"].get("to") if data.get("salary") else 0
        return result if result is not None else 0

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from < other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from >= other.salary_from

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from == other.salary_from
