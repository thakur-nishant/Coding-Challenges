def solution(A):
    count = 0
    pointer = 0
    while A[pointer] != -1:
        count += 1
        pointer = A[pointer]

    return count+1

A = [-1]
# A = [1,4,-1, 3,2]
x = solution(A)
print(x)