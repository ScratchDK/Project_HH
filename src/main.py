from src.auxiliary_functions import work_with_api, work_with_files


def main() -> None:
    """Функция отвечает за диалог с пользователем, давая возможность использовать основной функционал приложения"""
    print("Добро пожаловать!")
    print("Вы хотите получить список вакансий с сайта hh.ru или удалить вакансию из файла?")

    user_input_choice = ""

    while user_input_choice not in ['hh', 'удалить']:
        user_input_choice = input(
            "Введите 'hh' чтобы начать работу с api или 'удалить' для удаления вакансии из файла: ").lower()

    if user_input_choice == "hh":
        work_with_api()
    elif user_input_choice == "удалить":
        work_with_files()


if __name__ == "__main__":
    main()
