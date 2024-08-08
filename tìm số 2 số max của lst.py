lst = []
n = int(input('nhập só lượng phần tử của list: '))
while len(lst) < n:
    lst.append(int(input()))
lst.sort()
print(lst[-1], lst[-2])