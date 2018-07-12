from collections import Counter


def solution(A, K, M):
    row_list = [" "] * len(A)
    exact_long_row = []
    for i in range(len(A)):
        row_string = ""
        row_list[A[i] - 1] = 1
        num_long_row = 0
        for j in row_list:
            row_string += str(j)
        row_group = row_string.split()
        row_dict = Counter(row_group)
        for key in row_dict:
            if len(key) >= K:
                num_long_row += row_dict[key]

        if num_long_row == M:
            exact_long_row.append(i + 1)

    if exact_long_row:
        return max(exact_long_row)
    else:
        return -1


A = [2, 3, 7, 8, 10, 6, 4, 5, 9, 1]
K = 3
M = 2
x = solution(A, K, M)
print(x)
