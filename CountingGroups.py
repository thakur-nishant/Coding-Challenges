
def countGroups(m,t):

    visited = [[0]*len(m[0]) for _ in range(len(m))]
    log = {}
    for key in t:
        log[key] = 0

    def dfs(i, j):
        if visited[i][j] or m[i][j] == 0:
            visited[i][j] = 1
            return 0
        visited[i][j] = 1
        result = 1
        if i > 1:
            result += dfs(i - 1, j)
        if i < len(m) - 1:
            result += dfs(i + 1, j)
        if j > 1:
            result += dfs(i, j - 1)
        if j < len(m[0]) - 1:
            result += dfs(i, j + 1)

        return result

    for i in range(len(m)):
        for j in range(len(m[0])):
            if not visited[i][j] and m[i][j]:
                curr = dfs(i,j)
                log[curr] += 1

    res = []
    for num in t:
        res.append(log[num])

    return res
