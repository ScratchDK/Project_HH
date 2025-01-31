from src.external_api import ConnectAPIHeadHunter
from src.vacancies import Vacancy
from src.working_with_files import JsonFileHandler


def sorted_by_salary(data: list) -> list:
    for el in data:
        if el["salary"] is None:
            el["salary"] = {"from": 0}
        elif el["salary"]["from"] is None:
            el["salary"]["from"] = 0

    new_list = sorted(data, key=lambda x: x["salary"]["from"], reverse=True)
    return new_list


def work_with_api():
    data_api = ConnectAPIHeadHunter()

    print()
    print("Вы выбрали работу с api hh.ru")
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

    print()
    for el in sorted_list:
        vacancy = Vacancy(el, list_vacancies)
        print(str(vacancy))

    print("Вы хотите сохранить данный список вакансий в файл?")

    user_input_add = ""

    while user_input_add not in ["да", "нет"]:
        user_input_add = input("Введите да или нет: ").lower()

    if user_input_add == "да":
        user_input_filename = input("Введите название файла: ")
        filename = user_input_filename + ".json" if user_input_filename.isalpha() else "default.json"

        json_handler = JsonFileHandler(filename)
        json_handler.write_data(list_vacancies)
        print("Данные записаны!")
        print("Завершение работы приложения")
    else:
        print("Завершение работы приложения")

# def work_with_files():
#     json_handler = JsonFileHandler()
#     json_handler.write_data(list_vacancies)
#     json_handler.delete_data("116345295")
#     json_read = json_handler.read_data()
#
#     for el in json_read:
#         print(el)


def main():
    print("Добро пожаловать!")
    print("Вы хотите получить список вакансий с сайта hh.ru или начать работу с файломами?")

    user_input_choice = ""

    while user_input_choice not in ['hh', 'файлы']:
        user_input_choice = input("Введите 'hh' чтобы начать работу с api или 'файлы' для работы с файлами: ").lower()

    if user_input_choice == "hh":
        work_with_api()
    else:
        pass


main()
