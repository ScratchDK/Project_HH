from src.vacancies import Vacancy


def test_comparisons(vacancy1, vacancy2):
    test_vacancy1 = Vacancy(vacancy1)
    test_vacancy2 = Vacancy(vacancy2)
    test_vacancy3 = Vacancy(vacancy2)
    test_vacancy4 = "empty"

    assert test_vacancy2 > test_vacancy1
    assert test_vacancy1 < test_vacancy2
    assert test_vacancy1 <= test_vacancy2
    assert test_vacancy2 >= test_vacancy3
    assert test_vacancy2 == test_vacancy3

    assert (test_vacancy1 > test_vacancy4) == "incorrect comparison"
    assert (test_vacancy1 < test_vacancy4) == "incorrect comparison"
    assert (test_vacancy1 <= test_vacancy4) == "incorrect comparison"
    assert (test_vacancy2 >= test_vacancy4) == "incorrect comparison"
    assert (test_vacancy2 == test_vacancy4) == "incorrect comparison"
