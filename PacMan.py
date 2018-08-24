def pacmanScore(mat):
    if not mat:
        return 0
    if not mat[0]:
        return 0
    len_row = len(mat)
    len_col = len(mat[0])
    score_matrix= [[0 for i in range(len_col+1)] for j in range(len_row+1)]
    for i in range(len_row):
        for j in range(len_col):
            score_matrix[i+1][j+1] = mat[i][j] + max(score_matrix[i+1][j], score_matrix[i][j+1])

    return score_matrix[len_row][len_col]

mat = [[0,3,2,8],
       [1,4,9,3],
       [6,2,2,0]]

# mat = [[0,5],[401,0]]
x = pacmanScore(mat)
print(x)

