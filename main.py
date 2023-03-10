import math
# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# **Input:**
# n = 700
# m = 750
# **Output:**
# 2

n = int(input("Введите n: "))
m = int(input("Введите m: "))

result = math.ceil(m / n)
print(result)


# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# **Input:**
# 20
# 21
# 22
#
# **Output:**
# 32