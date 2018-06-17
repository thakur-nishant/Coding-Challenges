def countIslands(A):
    matrix = [row + [0] for row in A]
    matrix.append([0 for i in range(len(A)+1)])
    result_matrix = [[0 for i in range(len(A[0]) + 1)] for j in range(len(A)+1)]
    for i in range(len(A)-1,-1,-1):
        for j in range(len(A[0])-1,-1,-1):
            if A[i][j] or min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]):
                result_matrix[i][j] = A[i][j] + result_matrix[i][j+1] + result_matrix[i+1][j]
                result_matrix[i][j + 1] = 0
                result_matrix[i + 1][j] = 0

    return result_matrix


A = [[1,1,1,1,1],[0,0,0,0,1],[0,0,1,1,0],[0,1,0,0,0],[1,1,1,1,0]]
x = countIslands(A)
print(x)
