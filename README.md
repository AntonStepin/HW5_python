При решении не забывайте, пожалуйста, про функции: каждая задача должна быть представлена в виде одной или цепочки функции
1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'абвгдейка - это передача' = >" - это передача"


2- Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""

3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
['python', 'c#']
[1,2]
Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
[(1,'PYTHON'), (2,'C#')]
Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
[(1,'PYTHON'), (102,'C#')]
Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах