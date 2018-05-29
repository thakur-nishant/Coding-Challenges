def solution(a, b, c):
    sum = 0
    for i in range(1, c + 1):
        if i % a == 0 and i % b == 0:
            sum += i
        elif i % a == 0:
            sum += i
        elif i % b == 0:
            sum += i

    return sum


x = solution(5, 7, 15)
print(x)
