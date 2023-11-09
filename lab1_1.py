# Варіант №9
#
#   Враховуючи ціле число n - кількість хвилин, що пройшли з опівночі,
#   - скільки годин і хвилин відображаються на екрані 24-годинного цифрового годинника?
#   Програма повинна друкувати два числа: кількість годин (від 0 до 23)
#   і кількість хвилин (від 0 до 59). Наприклад, якщо n = 150,
#   то після опівночі пройшло 150 хвилин, тобто зараз 2:30 ранку.
#   Так що програма повинна друкувати 2 30.
# 
# Дзюба Владислав

n = int(input("Введіть кількість хвилин: "))

# ділення без остачі
h = n // 60

# остача від ділення
m = n % 60

print(f"{h}:{m}")
