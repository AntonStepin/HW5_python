# 4- Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах


def rle (user_str:str):
    result = ""
    b_char = ""
    count = 1
    for char in user_str:
        if char != b_char:
            if b_char:
                if count == 1:
                    temp = ""
                else:
                    temp = count
                result += f"{temp}"+b_char
            count = 1
            b_char = char
        else:
            count+=1
    return result

def return_rle(user_code:str):
    count = ""
    result = ""
    for char in user_code:
        if char.isdigit():
            count+=char
        elif count.isdigit():
            result += char*int(count)
            count = ""
        else:
            result+=char
            count = ""
    return result


