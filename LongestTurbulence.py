def solution(A):
    i = 0
    n = len(A)
    if n == 1:
        return 1
    start = i
    result = 0
    while i < n:
        result = max(result, i - start + 1)
        print(start, i, result)
        if i == 0:
            if A[i] > A[i+1] or A[i] < A[i+1]:
                i += 1
            elif A[i] == A[i+1]:
                result = max(result, i - start)
                i += 1
                start = i
        elif i == n-1:
            if A[i-1] < A[i] or A[i-1] >A[i]:
                i += 1
            elif A[i] == A[i-1]:
                result = max(result, i - start)
                i += 1
                start = i
        elif A[i-1] < A[i] and A[i] > A[i+1]:
            i += 1
        elif A[i-1] > A[i] and A[i] < A[i+1]:
            i += 1
        elif A[i-1] == A[i] and A[i+1] == A[i]:
            result = max(result, i -start)
            i += 1
            start = i
        else:
            result = max(result, i - start + 1)
            start = i
            i += 1
    return result

# A = [1,2,1,2,1,2,1,2,1,2]
# A = [1,1,1,1]
A = [9,4,2,10,7,8,8,1,9,9]
x = solution(A)
print(x)
