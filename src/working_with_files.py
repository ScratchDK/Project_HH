import json
import os
from abc import ABC, abstractmethod
from typing import Any

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AbstractFileHandler(ABC):

    @abstractmethod
    def read_data(self) -> Any:
        """Получение данных из файла."""
        pass

    @abstractmethod
    def write_data(self, data: list) -> None:
        """Добавление данных в файл."""
        pass

    @abstractmethod
    def delete_data(self, key: str) -> None:
        """Удаление данных из файла по ключу."""
        pass


class JsonFileHandler(AbstractFileHandler):
    """Класс отвечает за работу с файлами, позволяя считывать, записывать и удалять данные в указанный файл"""

    def __init__(self, path_file="default.json"):
        self.__path_file = path_file

    def read_data(self) -> Any:
        """Получение данных из JSON-файла."""
        full_path_file = os.path.join(base_dir, "data", self.__path_file)

        try:
            with open(full_path_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
        except FileNotFoundError:
            return []

    def write_data(self, data: list) -> None:
        """Добавление данных в JSON-файл."""
        full_path_file = os.path.join(base_dir, "data", self.__path_file)

        read_data = self.read_data()
        existing_ids = {el['id'] for el in read_data}

        for el_write in data:
            if el_write.get("id") not in existing_ids:
                read_data.append(el_write)

        with open(full_path_file, 'w') as file:
            json.dump(read_data, file, ensure_ascii=False)

    def delete_data(self, key: str) -> None:
        """Удаление данных из JSON-файла по ключу."""
        full_path_file = os.path.join(base_dir, "data", self.__path_file)

        read_data = self.read_data()

        key_to_remove = 'id'
        value_to_remove = key

        data = [el for el in read_data if el.get(key_to_remove) != value_to_remove]

        with open(full_path_file, 'w') as file:
            json.dump(data, file, ensure_ascii=False)
