print('Задача 30', '=' * 40)
# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_number_from_console(message):
    check_input = False
    string_number = ''
    while not check_input:
        string_number = input(message)
        check_input = string_number.isdigit()
        if not check_input:
            print("Неккоректный ввод")

    return int(string_number)

def make_arithmetic_sequence(first_element, length, coefficient_d):
    result = [first_element]
    for index, number in enumerate(range(first_element, first_element + length - 1)):
        result.append(number + (index - 1) * coefficient_d)
    return result

def task_30():
    first_element = get_number_from_console('Введите первый элемент последовательности: ')
    length = get_number_from_console('Введите количество элементов последовательности: ')
    coefficient_d = get_number_from_console('Введите коэффициент d в формуле an = a1 + (n-1) * d: ')

    arithmetic_sequence = make_arithmetic_sequence(first_element, length, coefficient_d)
    print(arithmetic_sequence)

task_30()
print()

print('Задача 32', '=' * 40)
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]