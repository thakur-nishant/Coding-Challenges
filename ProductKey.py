def solution(S, K):
    # write your code in Python 3.6
    newS = S.upper().replace("-", "")
    count = 0
    result = ""
    print(newS, " ", K)
    for i in newS[::-1]:
        if (count == K):
            count = 1
            result += "-" + i
        else:
            result += i
            count += 1

    return result[::-1]



S = "2-4A0r7-4k"
K = 3
x = solution(S, K)
print(x)
