# дз 2
# задание 1 
'''
1) Создать скрипт для анализа тестовых файлов - сбора статистики упоминания слов. 

Аргументом командной строки является имя файла, который нужно проанализировать. 
Второй аргумент - количество слов, которые нужно выводить на экран (если аргумент не указан, то выводим статистику по 100 словам, статистика выводится в порядке убывания частоты слов, по каждому слову на экран выводится строка в формате "<слово> <частота>"). 
Если второй аргумент не целое число, то его рассматриваем как имя файла, в который в формате CSV с заголовком сохраняем статистику слов (Первый столбец - слово, второй столбце - частота).
'''

import sys
import string
import csv
from collections import Counter

def analyze_file(file_name, count=100):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text_str = file.read().lower()  # убираем заглавные буквы
            translator = str.maketrans({char: '' for char in string.punctuation})  # правила преобразования строки
            # .maketrans(dict) или .maketrans(char, to_char) или .maketrans(arg1, arg2, arg3)
            text_str = text_str.translate(translator)  # преобразование строки - убираем знаки пунктуации
            text_words = text_str.split()

            # класс collections.Counter() предназначен для удобных и быстрых подсчетов 
            # количества появлений неизменяемых элементов в последовательностях.
            # A Counter is a dict subclass for counting hashable objects.
            word_freq = Counter(text_words)  # имеет вид Counter({'str1': number1, 'str2': number2, ...})
            sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)  # сортируем по количеству вхождений слова в тексте

            if isinstance(count, int):  # пренадлежит ли count к типу int
                output_words = sorted_freq[:count]
                for word, freq in output_words:
                    print(f"{word} {freq}")
            else:
                try:
                    with open(count, mode='w', newline='') as file_csv:  # если нам нужно создать csv файл с именем count
                        writer = csv.writer(file_csv)
                        writer.writerow(['слово', 'частота'])
                        writer.writerows(sorted_freq)
                except:
                    print(f'нельзя сохранить в файл \'{count}\' или ошибка при сохранении в \'{count}\'')
                    return
    except:
        print(f'\n ~ ошибка при считывании из \'{file_name}\' или файл \'{file_name}\' нельзя открыть ~ \n')
        return


if __name__ == "__main__":
    # argv - список аргументов командной строки
    # argv[0] - имя скрипта - всегда и везде
    # argv[1] - имя файла откуда берем инфу
    # argv[2] - если есть, то количество строк/ название файла куда сохранить информацию
    
    if len(sys.argv) < 2:
        print('\n ~ неправильные аргументы ~ \n')
        sys.exit()  # выход из Python, поднятие исключения SystemExit (искл можно перехватить)
    elif len(sys.argv) == 3:
        try:
            count = int(sys.argv[2])
        except ValueError:
            count = sys.argv[2]
        analyze_file(sys.argv[1], count)
    else:
        analyze_file(sys.argv[1])