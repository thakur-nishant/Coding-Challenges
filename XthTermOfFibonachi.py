def solution(x):
    a = 1
    b = 1
    index = 2

    if x < 2:
        return x * chr(96 + x)
    while index <= x:
        c = a + b
        a, b = b, c
        index += 1

    return c * chr(96 + x)


result = solution(4)
print(result)
