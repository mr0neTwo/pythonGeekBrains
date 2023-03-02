import random

print('Задача 22', '=' * 40)
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

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

def task_22():
    n = get_number_from_console('Введите число n(длина первого множества): ')
    m = get_number_from_console('Введите число m(длина второго множества): ')

    list_n = get_random_array(n)
    list_m = get_random_array(m)

    set_n = set(list_n)
    set_m = set(list_m)

    result = set_n.intersection(set_m)
    result = list(result).sort()

    print('Список от n:', list_n)
    print('Список от m:', list_m)
    print('Результат:')
    print(result)

task_22()
print()


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один
# заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

def task_24():
    n = get_number_from_console('Введите число N(количество кустов): ')
    bushes = get_random_array(n)

    if n < 3:
        max_value = sum(bushes)
    else:
        max_value = bushes[0] + bushes[-1] + bushes[-2] # расчет последней итерации не вошедшей из-за len(bushes) - 1
        for i in range(0, len(bushes) - 1):
            received_berry = bushes[i - 1] + bushes[i] + bushes[i + 1]
            if received_berry > max_value:
                max_value = received_berry + 0

    print('Грядка:', bushes)
    print('Максимально возможный сбор:', max_value)

task_24()

