def solution_DP(matrix):
    if not matrix:
        return 0
    if not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])

    path = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                path[i][j] = 1
            elif matrix[i][j] == 1:
                if i > 0 and matrix[i-1][j]:
                    path[i][j] += path[i-1][j]
                if j > 0 and matrix[i][j-1]:
                    path[i][j] += path[i][j-1]

    return path[rows-1][cols-1]


def solution_DFS(matrix):
    if not matrix:
        return 0
    if not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])

    i = j = 0
    count = recur_util(i, j, matrix, rows, cols)

    return count


def recur_util(i, j, matrix, rows, cols):
    if i == rows - 1 and j == cols - 1:
        return 1
    down = right = 0
    if i+1 < rows and matrix[i+1][j]:
        down = recur_util(i+1, j, matrix, rows, cols)
    if j+1 < cols and matrix[i][j+1]:
        right = recur_util(i, j+1, matrix, rows, cols)

    return down + right


matrix = [[1]]
# matrix = [[1,1,0,1], [1,1,1,1]]
# matrix = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
x = solution_DFS(matrix)
print("DFS Solution:", x)

y = solution_DP(matrix)
print("DP Solution:", y)

