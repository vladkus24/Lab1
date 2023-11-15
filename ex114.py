# Напишіть програму, щоб перевірити, чи є введене число додатним, від’ємним або це нуль.

n = int(input("Введіть число: "))

if n > 0:
    print("It is positive number")
elif n == 0:
    print("It is zero")
else:
    print("It is negative") 