import constants as settings
from utils import display_menu, read_input


def main():
    initial_values = input("Enter initial list values: ")
    separator = input("Separate values by: ")
    lst = initial_values.split(separator)

    while True:
        print(display_menu("\n", settings.menu))
        choice = input(settings.enter_choice_msg)

        if not settings.choices_menu.get(choice):
            print("Invalid choice. Please try again.")
            continue


        operations_dict = settings.choices_menu[choice]
        user_inputs = read_input(operations_dict["input_msgs"])
        lst = operations_dict["executor"](lst, *user_inputs)
        print(lst)


if __name__ == "__main__":
    main()
