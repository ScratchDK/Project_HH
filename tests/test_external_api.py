import pytest
from unittest.mock import patch

from src.external_api import ConnectAPIHeadHunter


def test_get_vacancies_with_valid_params(capsys, data_api):
    api = ConnectAPIHeadHunter()

    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": data_api
        }

        vacancies = api.get_vacancies("Пятигорск", "3")

        massage = capsys.readouterr()

        assert massage.out.strip() == 'Подключение к API HeadHunter установлено успешно!'
        assert len(vacancies) == 3
        assert vacancies[0]['name'] == 'Руководитель группы магазинов'
        assert vacancies[1]['name'] == 'Директор сети магазинов'
        assert vacancies[2]['name'] == 'Администратор'


@pytest.mark.parametrize("page, excepted", [("200", 200), ("-10", -10)])
def test_get_vacancies_with_invalid_per_page(page, excepted, data_api):
    api = ConnectAPIHeadHunter()

    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": data_api}

        vacancies = api.get_vacancies(text="менеджер", per_page=page)

        assert len(vacancies) != excepted


def test_failed_connection(capsys):
    api = ConnectAPIHeadHunter()

    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        api._connect()

        massage = capsys.readouterr()

        assert massage.out.strip() == 'Ошибка подключения к API HeadHunter, код ошибки: 404'
