def cal(a, b=3):

    sum = a + b

    sub = a - b

    mul = a * b

    return sum, sub, mul

s, sub, mul = cal(6)

print(s, mul, sub)