# find length of shortest path from point A to point B in a matrix;

def shortest_path_in_matrix(matrix, A, B):
    q = []
    visited = set()
    q.append((A[0], A[1], 0))
    row_len = len(matrix)
    col_len = len(matrix[0])
    while q:
        x, y, steps = q.pop(0)

        if (x, y) in visited:
            continue
        if [x, y] == B:
            return steps
        if 0 <= x < row_len and 0 <= y < col_len and matrix[x][y] == 1:
            visited.add ((x,y))
            q.append((x - 1, y, steps + 1))
            q.append((x + 1, y, steps + 1))
            q.append((x, y + 1, steps + 1))
            q.append((x, y - 1, steps + 1))
    print(q)


mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
       [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
       [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]

a = [0, 0]
b = [5, 7]
result = shortest_path_in_matrix(mat, a, b)
print(result)
