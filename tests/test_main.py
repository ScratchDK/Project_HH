import pytest
from unittest.mock import patch

from src.main import main
from src.working_with_files import JsonFileHandler


@pytest.mark.parametrize(
    "user_input, answer, answer2, len_vacancies",
    [
        (["hh", "Пятигорск", "3", "нет", "нет"], "Вы выбрали работу с api hh.ru", 'РУКОВОДИТЕЛЬ ГРУППЫ МАГАЗИНОВ', 3),
        (["удалить", "test", "116566958", "116627013", "выход"], "Вы выбрали работу с файлами",
         "{'id': '116285274', 'name': 'Администратор', "
         "'salary': {'from': 50000, 'to': None}, "
         "'address': {'raw': 'Пятигорск, Бештаугорское шоссе'}, "
         "'alternate_url': 'https://hh.ru/vacancy/116285274', "
         "'snippet': {'requirement': None, 'responsibility': 'Прием звонков компании. "
         "-Контроль исполнения заданий и поручений. -Техническое обеспечение работы офиса.'}}", 1),
        (["hh", "Пятигорск", "3", "да", "да", "test"], "Вы выбрали работу с api hh.ru", 'ДИРЕКТОР СЕТИ МАГАЗИНОВ', 3)
    ],
)
def test_multiple_inputs(capsys, user_input: list, answer, answer2, len_vacancies: int, data_api: list) -> None:
    api = JsonFileHandler("test.json")
    api.write_data(data_api)

    with patch("builtins.input", side_effect=user_input), patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": data_api
        }

        main()

        read_data = api.read_data()

        massage = capsys.readouterr()

        assert massage.out.strip().split("\n")[3] == answer
        assert massage.out.strip().split("\n")[10] == answer2
        assert len(read_data) == len_vacancies


def test_invalid_keywords(capsys):
    with patch("builtins.input", side_effect=["hh", "qwerty123", "1"]):
        main()

        massage = capsys.readouterr()

        assert massage.out.strip().split("\n")[-2] == "Извините, но по вашему запросу вакансии не найдены!"
        assert massage.out.strip().split("\n")[-1] == "Завершение работы приложения"
