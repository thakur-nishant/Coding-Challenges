def matrixRotation(A):
    if not A:
        return A
    if not A[0]:
        return A
    row = len(A)
    col = len(A[0])
    result = [[0 for i in range(row)] for j in range(col)]
    for i in range(col):
        for j in range(row):
            result[i][row -j -1] = A[j][i]
    return result

A = [[1,2,3],
     [4,5,6],
     [7,8,9]
    ]
x = matrixRotation(A)
print(x)

