# дз 2
# задание 2

import sys
import csv

import string
from collections import Counter

'''
2) Создать скрипт, которому в командной строке передаются имена файлов. 

В файлах в формате CSV с заголовком содержится информация о частоте слов: первый столбец - слово, второй столбце - частота. 

Выполнить агрегацию информации о частоте слов из всех переданных файлов (т.е. рассчитать суммарную частоту для всех упомянутых слов). 

Результат сохранить в файл с именем, которое введет пользователь в ответ на соответствующий запрос.

2.1) Скрипт должен адекватно реагировать на ситуацию отсутствия файлов и другие проблемы с вводом/выводом.
2.2) Оформить модуль с функциями, которые используются в задании 1 и 2.

'''
# функция из 1) для создания модуля из этого файла
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


def aggregate_files(file_names):
    word_freq = {}
    for file_name in file_names:
        # в словарь word_freq добавляем новые слова или обновляем частоту для каждого файла из списка файлов 
        try:
            with open(file_name, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # пропускаем первую строку - заголовок
                for row in csv_reader:
                    word, freq = row[0].split(';')  # разделяем ';' т.к. такой разделитель в моих файлах
                    word_freq[word] = word_freq.get(word, 0) + int(freq)  # добавляем частоту слов в данном файле к общей сумме
                                                                          # .get(ключ, значение default = 0)    ->    {'ключ': 0}
        except:
            print(f'\n ~ ошибка при считывании из \'{file_name}\' или файл \'{file_name}\' нельзя открыть ~ \n')
            return

    # имя файла для сохранения
    output_file = input('имя файла для сохранения результата: ')
    # сохраняем  в указанный файл
    try:
        with open(output_file, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=';')  # ра зделяем ';' т.к. такой формат поймет excel
            csv_writer.writerow(['слово', 'суммарная частота'])  # добавляем заголовок
            for word, freq in word_freq.items():
                csv_writer.writerow([word, freq])  # добавляем элементы
        print(f'результат сохранен в {output_file}')
    except:
        print(f'нельзя сохранить в файл \'{output_file}\' или ошибка при сохранении в \'{output_file}\'')
        return


if __name__ == "__main__":
    # argv - список аргументов командной строки
    
    if len(sys.argv) < 2:
        # если ни один файл для считывания не указан
        print('\n ~ неправильные аргументы ~ \n')
        sys.exit()  # выход из Python, поднятие исключения SystemExit (искл можно перехватить)
    aggregate_files(sys.argv[1:])