import view

encoding_format = 'UTF-8'


def add_data(data):
    with open(file='database.txt', mode='a', encoding=encoding_format) as file:
        file.write(data)


def find_data(search_data):
    with open(file='database.txt', mode='r', encoding=encoding_format) as file:
        data_list = file.readlines()

    search_data = search_data.lower()
    result = list(filter(lambda x: search_data in x, data_list))

    if not result:
        print('По вашему запросу данные не найдены')

    return result


def change_row(result):
    print('Введите номер строки, которую хотите изменить')
    view.print_result(result)
    index = view.get_index_from_console(len(result))
    old_row = result[index - 1]
    new_row = view.get_data()
    all_data = find_data('')
    index = all_data.index(old_row)
    all_data[index] = new_row

    with open(file='database.txt', mode='w', encoding=encoding_format) as file:
        file.write(''.join(all_data))


def delete_row(result):
    print('Введите номер строки, которую хотите удалить')
    view.print_result(result)
    index = view.get_index_from_console(len(result))
    row = result[index - 1]
    all_data = find_data('')
    all_data.remove(row)

    with open(file='database.txt', mode='w', encoding=encoding_format) as file:
        file.write(''.join(all_data))

    print('Запись удалена')
