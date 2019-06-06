def minimumDistance(numRows, numColumns, area):

    if not any(area):
        return -1
    queue = [(0, 0, 0)]
    visited = [[0]*numColumns for _ in range(numRows)]
    while queue:
        i, j, dist = queue.pop(0)
        if 0 <= i < numRows and 0 <= j < numColumns and area[i][j] and not visited[i][j]:
            visited[i][j] = 1
            if area[i][j] == 9:
                return dist
            queue.append((i - 1, j, dist + 1))
            queue.append((i + 1, j, dist + 1))
            queue.append((i, j - 1, dist + 1))
            queue.append((i, j + 1, dist + 1))
    return -1


area = [
    [1,1,1,1],
    [0,1,1,1],
    [0,1,0,1],
    [1,1,9,1],
    [0,0,1,1]
]

r = 5
c = 4

print(minimumDistance(r,c,area))
