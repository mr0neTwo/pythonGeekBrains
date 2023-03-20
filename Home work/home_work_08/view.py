
def get_operation():
    print('\n1 - записать\n2 - прочитать\n3 - изменить\n4 - удалить\n5 - выход\n')
    operation = int(input())
    return operation


def get_data():
    print('Введите данные')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    phone = input('Телефон: ')
    row = f'{name} {surname} {phone}\n'
    return row


def get_search_data():
    search_data = input('Введите запрос: ')
    return search_data


def print_result(result):
    for n, row in enumerate(result, 1):
        print(f'{n} - {row.rstrip()}')


def get_index_from_console(max_index):
    condition = True
    number = None
    while condition:
        string_number = input()
        check_input = string_number.isdigit()
        if not check_input:
            print("Некорректный ввод, поробуйте снова")
        else:
            number = int(string_number)
            if 0 < number <= max_index:
                condition = False
            else:
                print("Записи с таким индексом не существут, поробуйте снова")

    return number
