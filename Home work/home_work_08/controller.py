import view
import database


def main():
    is_input_exit = False
    while not is_input_exit:

        operation = view.get_operation()

        if operation == 1:
            employee_data = view.get_data()
            database.add_data(employee_data)

        elif operation == 2:
            search_data = view.get_search_data()
            result = database.find_data(search_data)
            if result:
                view.print_result(result)

        elif operation == 3:
            search_data = view.get_search_data()
            result = database.find_data(search_data)
            if result:
                database.change_row(result)

        elif operation == 4:
            search_data = view.get_search_data()
            result = database.find_data(search_data)
            if result:
                database.delete_row(result)

        elif operation == 5:
            is_input_exit = True

        else:
            print('Введенная с указанным номером не существует')


if __name__ == '__main__':
    main()
