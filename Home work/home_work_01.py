# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def get_3digit_from_console():
    check_input = False
    string_digit = ''
    while not check_input:
        string_digit = input("Введетие трехзначное чилсло: ")
        check_input = len(string_digit) == 3 and string_digit.isdigit()
        if not check_input:
            print("Неккоректный ввод")

    return string_digit


def sum_of_number_digits(string_digit):
    sum_digits = 0
    for digit in string_digit:
        sum_digits += int(digit)
    return sum_digits


string_digit = get_3digit_from_console()
result = sum_of_number_digits(string_digit)
print(f'Сумма цифер чилса {string_digit} равна {result}')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def get_number_from_console(message):
    check_input = False
    string_number = ''
    while not check_input:
        string_number = input(message)
        check_input = string_number.isdigit()
        if not check_input:
            print("Неккоректный ввод")

    return int(string_number)


def print_count_child_origami(amount):
    if amount % 6 == 0:
        kate_count = amount // 3 * 2
        sergey_peter_count = amount // 6
        print(f'Катя сделала {kate_count} журавликов')
        print(f'Сережа и Петя сделали по {sergey_peter_count} журавликов')
    else:
        print('Введенной число не соответсвует условниям задачи')


s = get_number_from_console('Введите число журавликов, которые сделали дети: ')
print_count_child_origami(s)


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

def is_happy_ticket(ticket_number):
    string_ticket_number = str(ticket_number)
    len_number = len(string_ticket_number)

    if len_number % 2 != 0:
        return False

    lef_part = string_ticket_number[: len_number // 2]
    right_part = string_ticket_number[len_number // 2:]

    left_sum = sum(map(lambda digit: int(digit), lef_part))
    right_sum = sum(map(lambda digit: int(digit), right_part))

    return left_sum == right_sum


ticket_number = get_number_from_console("Введеите номер билета: ")
print(f'Билет с номером {ticket_number} {"" if is_happy_ticket(ticket_number) else "не"}счастливый')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def can_break_of_peace(size, part):
    return part % size[0] == 0 or part % size[1] == 0

size = [
    get_number_from_console("Введеите длину шокаладки: "),
    get_number_from_console("Введеите ширину шоколадки: ")
]
part = get_number_from_console("Введеите количество долек: ")

result_word = 'можно' if can_break_of_peace(size, part) else 'нельзя'
print(f'От шоколадки с размером {size[0]}x{size[1]} {result_word} отломить {part} долек')