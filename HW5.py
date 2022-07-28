# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

import random

def record_text_in_file(text:str):
    with open('file.txt', "w") as file_txt:
        file_txt.writelines(text)

def remove_unnecessary_word(part_of_word: str, text: str):
    result = " "
    path = text
    with open(path,"r") as source:
        for line in source:
            temp = line.split(" ")
            for value in temp:
                if not part_of_word in value:
                    result += f"{value} "
    with open(path, "w") as text_file:
        text_file.writelines(result)

