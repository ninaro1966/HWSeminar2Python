#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# N - 6782 -> 23
# - 0,56 -> 11
float_num = input('Ввведите вещественное число: ')

sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print(f'Сумма диджитов в числе: {sum}')