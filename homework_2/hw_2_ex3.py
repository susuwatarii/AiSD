# дз 2
# задание 3

'''
3.1) Написать программу, которая запускается из консоли и считает сумму переданных в неё чисел

3.2) Добавить в эту программу произведение
3.3) По переданному параметру считать либо сумму, либо произведение
3.4) Оформить это дополнительный модуль.
'''

import sys


def sum_of_n(numbers):
    # сумма чисел
    sum_of_numbers = 0.0
    for numb in numbers:
        try:
            sum_of_numbers += float(numb)
        except:
            print('\n ~ не все аргументы - числа! ~ \n')
            return
    return sum_of_numbers


def mult_of_n(numbers):
    # произведение чисел
    mult_of_numbers = 1
    for numb in numbers:
        try:
            mult_of_numbers *= float(numb)
        except:
            print('\n ~ не все аргументы - числа! ~ \n')
            return
    return mult_of_numbers


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # если ни одно число не указано
        print('\n ~ неправильные аргументы ~ \n')
        sys.exit()  # выход из Python, поднятие исключения SystemExit (искл можно перехватить)
        
    # argv[1] - выбираем тип действия
    match sys.argv[1]:
        case 'sum':
            print(sum_of_n(sys.argv[2:]))
        case 'mult':
            print(mult_of_n(sys.argv[2:]))
        case _:
            print('\n ~ вы не выбрали ни умножение, ни сумму ~ \n')