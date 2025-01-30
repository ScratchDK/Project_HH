from src.external_api import ConnectAPIHeadHunter
from src.vacancies import Vacancy
from src.working_with_files import JsonFileHandler


def main():
    data_api = ConnectAPIHeadHunter()

    print("Добро пожаловать!")
    print("По каким ключевым словам вы хотите отсортировать вакансий?\n"
          "Введите ключевые слова через запятую! Например: 'Москва, Python разработчик'.")
    user_input_word = input("Введите ключевые слова: ")
    user_input_page = input("Введите количество вакансий для отображения: ")
    get_vacancies = data_api.get_vacancies(user_input_word, user_input_page)

    list_vacancies = []

    for el in get_vacancies:
        vacancy = Vacancy(el, list_vacancies)
        print(str(vacancy))

    vacancy1 = Vacancy(get_vacancies[0])
    print(f"vacancy1 = {vacancy1}")

    vacancy2 = Vacancy(get_vacancies[1])
    print(f"vacancy1 = {vacancy2}")

    print(f"СРАВНЕНИЕ {vacancy1 >= vacancy2}")

    json_handler = JsonFileHandler()
    json_handler.write_data(list_vacancies)
    json_handler.delete_data("116345295")
    json_read = json_handler.read_data()

    for el in json_read:
        print(el)


main()
