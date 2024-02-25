# дз 2
# задание 4

'''
4) Реализовать модуль calculate.py, содержащий набор функций для работы с целыми числами, записанными как на русском языке (например: тридцать восемь), так и в виде простых арифметических выражений (например: 2 + 3).
На базе этого модуля подготовить скрипт calculate.py со следующими возможностями:
1) python claculate.py to_numbers my_file.txt
Вызов приводит к преобразованию всех чисел, написанных на русском языке в числовом виде и сохранению изменений в файл с тем же именем.
python claculate.py to_numbers my_file.txt my_file_res.txt
(результат сохраняется в файл с именем my_file_res.txt)

'''
import words2numsrus
import re


def evaluate_arithm_exp(text):
    pattern = r'\b(\d+)\s*([-+*/])\s*(\d+)\b'

    def replace_expr(match):
        return str(eval(match.group(0)))

    evaluated_text = re.sub(pattern, replace_expr, text)
    return evaluated_text


def to_numbers(argv_1, input_file, output_file=None):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    converted_text = ''
    if argv_1 == 'rus':
        extractor = words2numsrus.NumberExtractor()
        converted_text = extractor.replace_groups(text)
    elif argv_1 == 'math':
        converted_text = evaluate_arithm_exp(text)
    else:
        print(' некорректный аргумент 1 ')
        return
    
    if not output_file:
        output_file = input_file
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(converted_text))
        

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\n неправильное количество аргументов \n")
        sys.exit()
    
    input_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) == 4 else sys.argv[2]
    
    to_numbers(argv[1], input_file, output_file)

'''
1. r перед строкой указывает на "сырую" строку (raw string) в Python, что позволяет нам избежать необходимости экранирования обратных слэшей.
2. \b - это метасимвол для границы слова, который указывает на начало или конец слова.
3. (\d+) - это группа, которая соответствует последовательности одного или более цифр. \d обозначает любую цифру, а + означает одно или более повторений цифры.
4. \s* - это пробелы (или другие пробельные символы), которые могут быть, но не обязательно, после первой группы цифр. \s обозначает любой пробельный символ, а * означает ноль или более повторений.
5. ([-+*/]) - это группа, которая соответствует одному из символов: "-", "+", "*", "/".
6. \s* - опять же, пробелы между оператором и следующей цифрой.
7. (\d+) - еще одна группа цифр (аналогичная первой группе).
8. \b - граница слова в конце, чтобы гарантировать, что после второй цифры идет конец выражения.
'''