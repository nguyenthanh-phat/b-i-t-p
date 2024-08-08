lst = []
n = int(input('nhập số lượng phần tử của mảng: '))
while len(lst) < n:
    lst.append(int(input()))

print(min(lst))