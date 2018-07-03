def solution(S, T):
    i, j = 0, 0
    while j < len(T) and i < len(S):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(T):
        return 1
    return 0

print(solution('abjfkaskjfabcdfnjf','abcd'))