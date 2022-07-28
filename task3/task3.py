# record_text_in_file("абвгдейка - это передача")
# remove_unnecessary_word("абв", "file.txt")

# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре 
# в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой 
# таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком


def create_two_list(path):
    language_list = [line.strip() for line in open(path)]
    number_list = [x for x in range (1, len(language_list)+1)]
    return [number_list, language_list ]

def tuples_number_lang(number: list, language: list):
    tup_lst = [(number[i], str.upper(language[i])) for i in range (0, len(number))]
    return tup_lst

def main_sum_points(tup_lst: tuple):
    sum = 0
    result = []
    for i in range (0, len(tup_lst)):
        points = 0
        for char in (tup_lst[i][1]):
            points += int(ord(char))
        if points%tup_lst[i][0] == 0:
            temp = (points, tup_lst[i][1])
            result.append(temp)
            sum+=points
    return [result, sum]

# path = "task3\language.txt"
# tup_lst = tuples_number_lang((create_two_list(path)[0]), (create_two_list(path)[1]))
# print(main_sum_points(tup_lst))

