def minJumpToReachEnd(A):
    i = 1
    n = len(A)
    record = [None] * n
    history = [None] * n
    record[0] = 0
    history[0] = -1
    while i < n:
        j = 0
        while j < i:
            if A[j] >= i - j:
                if record[i]  and (record[i] > record[j] + 1):
                    record[i] = record[j] + 1
                    history[i] = j
                elif record[i] is None:
                    record[i] = record[j] + 1
                    history[i] = j
            j += 1
        i += 1

    print(record)
    print(history)


A = [2,3,1,1,2,4,2,0,1,1]
minJumpToReachEnd(A)
