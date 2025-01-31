from src.external_api import ConnectAPIHeadHunter
from src.vacancies import Vacancy
from src.working_with_files import JsonFileHandler


def check_key_salary(key):
    if key["salary"]["from"]:
        return


def sorted_by_salary(data: list) -> list:
    for el in data:
        if el["salary"] is None:
            el["salary"] = {"from": 0}
        elif el["salary"]["from"] is None:
            el["salary"]["from"] = 0

    new_list = sorted(data, key=lambda x: x["salary"]["from"], reverse=True)
    return new_list


def main():
    data_api = ConnectAPIHeadHunter()

    print("Добро пожаловать!")
    print("По каким ключевым словам вы хотите отсортировать вакансий?\n"
          "Введите ключевые слова через запятую! Например: 'Москва, Python разработчик'.")
    user_input_word = input("Введите ключевые слова: ")
    user_input_page = input("Введите количество вакансий для отображения: ")
    get_vacancies = data_api.get_vacancies(user_input_word, user_input_page)

    if not get_vacancies:
        print("Извините, но по вашему запросу вакансии не найдены!")

    print("Вы хотите отсортировать вакансий по зарплате (от большей к меньшей)?")

    user_input_sort = ''

    while user_input_sort not in ["да", "нет"]:
        user_input_sort = input("Введите да или нет: ").lower()

    if user_input_sort == "да":
        sorted_list = sorted_by_salary(get_vacancies)
    else:
        sorted_list = get_vacancies

    list_vacancies = []

    for el in sorted_list:
        vacancy = Vacancy(el, list_vacancies)
        print(str(vacancy))

    # vacancy1 = Vacancy(get_vacancies[0])
    # print(f"vacancy1 = {vacancy1}")
    #
    # vacancy2 = Vacancy(get_vacancies[1])
    # print(f"vacancy1 = {vacancy2}")
    #
    # print(f"СРАВНЕНИЕ {vacancy1 >= vacancy2}")

    json_handler = JsonFileHandler()
    json_handler.write_data(list_vacancies)
    json_handler.delete_data("116345295")
    json_read = json_handler.read_data()

    for el in json_read:
        print(el)


main()
