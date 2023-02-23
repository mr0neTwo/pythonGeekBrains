import random

print('Задача 10', '=' * 40)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = random.randint(0, 101)
coin_sides = ['head', 'tail']
list_coins = [random.choice(coin_sides) for coin in range(0, n)]

count_head = list_coins.count('head')
count_tail = len(list_coins) - count_head
result = count_head if count_head < count_tail else count_tail

print('Длина списка:', len(list_coins))
print('Количество решек:', count_tail)
print('Количество орлов:', count_head)
print('Минимальное количество монет, которые нужно перевернуть:', result)
print()

print('Задача 12', '=' * 40)
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

max_value = 1001
x_number = random.randint(0, max_value)
y_number = random.randint(0, max_value)

s = x_number + y_number
p = x_number * y_number
print(f'Сумма чисел:', s)
print(f'Произведение чисел:', p)

for x in range(0, max_value):
    for y in range(0, max_value):
        if x * y == p and x + y == s:
            print(f'x = {x}, y = {y}')
            break
    if x * y == p and x + y == s:
        break

print(f'Загаданные значения: x = {x_number}, y = {y_number}')
print()

print('Задача 14', '=' * 40)
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

max_value = 100000
n = random.randint(0, max_value)
print('n =', n)
p = 1
while 2**p < max_value:
    print(2**p)
    p += 1

