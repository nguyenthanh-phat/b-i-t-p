def calculate(a):
    results = []  
    for i in range(1, 11):
        kqua = a * i
        results.append(kqua)  
    return results

n = int(input('Nhập số: '))
results = calculate(n)
for i, result in enumerate(results, start=1):
    print(f"{n} x {i} = {result}")
