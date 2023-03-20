import random

print('Задача 16', '=' * 40)
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


def get_random_array(array_len):
    return [random.randint(0, 10) for x in range(array_len)]


def get_number_from_console(message):
    check_input = False
    string_number = ''
    while not check_input:
        string_number = input(message)
        check_input = string_number.isdigit()
        if not check_input:
            print("Неккоректный ввод")

    return int(string_number)

def task_16():
    n = get_number_from_console('Введите число N(длина списка) : ')
    x = get_number_from_console('Введите число X(искомое число): ')

    array = get_random_array(n)
    count_x = array.count(x)

    print(array)
    print(f'Число {x} встречается в данном массиве {count_x} раз')

task_16()
print()

print('Задача 18', '=' * 40)
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

def task_18():
    n = get_number_from_console('Введите число N(длина списка) : ')
    x = get_number_from_console('Введите число X(искомое число): ')

    array = get_random_array(n)
    closest_number = array[0]
    min_different = abs(x - array[0])
    for number in array[1:]:
        if abs(x - number) < min_different:
            min_different = abs(x - number)
            closest_number = number

    print(array)
    print(f'Самое близкое число к числу {x} в данном массиве является число {closest_number}')

task_18()
print()

print('Задача 20', '=' * 40)
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*
#
# ноутбук
#     12

letters_value_en = [
    {
        'letters': ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
        'value': 1
    }, {
        'letters': ['D', 'G'],
        'value': 2
    }, {
        'letters': ['B', 'C', 'M', 'P'],
        'value': 3
    }, {
        'letters': ['F', 'H', 'V', 'W', 'Y'],
        'value': 4
    }, {
        'letters': ['K'],
        'value': 5
    }, {
        'letters': ['J', 'X'],
        'value': 8
    }, {
        'letters': ['Q', 'Z'],
        'value': 1
    }
]
letters_value_rus = [
    {
        'letters': ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
        'value': 1
    }, {
        'letters': ['Д', 'К', 'Л', 'М', 'П', 'У'],
        'value': 2
    }, {
        'letters': ['Б', 'Г', 'Ё', 'Ь', 'Я'],
        'value': 3
    }, {
        'letters': ['Й', 'Ы'],
        'value': 4
    }, {
        'letters': ['Ж', 'З', 'Х', 'Ц', 'Ч'],
        'value': 5
    }, {
        'letters': ['Ш', 'Э', 'Ю'],
        'value': 8
    }, {
        'letters': ['Ф', 'Щ', 'Ъ'],
        'value': 1
    }
]

def word_value(word, value_rules):
    word = word.upper()
    word_value = 0
    for letter in word:
        for rule in value_rules:
            if letter in rule['letters']:
                word_value += rule['value']
    return word_value

def task_20():
    print('0 - Русский')
    print('1 - English')
    mode = get_number_from_console('Выберете режим/Select a mode: ')

    if mode != 0 and mode != 1:
        print('Выбранный режим не существует')
        print('The selected mode does not exist')
    else:
        letters_value = letters_value_en if mode else letters_value_rus
        word = input('Type the word: ')
        result = word_value(word, letters_value)
        print(f'Value of "{word}" is {result} point')

task_20()

