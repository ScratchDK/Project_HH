import pytest

from src.working_with_files import JsonFileHandler


@pytest.mark.parametrize("filename", ["no_found.json", "empty.json"])
def test_not_found_error(filename):
    api = JsonFileHandler(filename)
    result = api.read_data()

    assert result == []
