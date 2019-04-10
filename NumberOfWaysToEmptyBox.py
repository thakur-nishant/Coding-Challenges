def countWays(N):
    arr = [1,3]
    m = len(arr)
    count = [0 for i in range(N + 1)]

    count[0] = 1

    for i in range(1, N + 1):
        for j in range(m):
            if i >= arr[j]:
                count[i] += count[i - arr[j]]
    return count[N]


print(countWays(7))
