def count_chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result

chuoi = input('nhập chuỗi: ')
print(count_chars(chuoi))