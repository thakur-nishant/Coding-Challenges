"""
Consider an undirected tree with N nodes, numbered from 1 to N. Each node has a label associated with it, which is an integer value. Different nodes can have the same label. Write a function that, given a zero indexed array A of length N, where A[j] is the label value of the (j + 1)-th node in the tree and a zero-indexed array E of length K = (N – 1) * 2 in which the edges of the tree are described, returns the length of the longest path such that all the nodes on that path have the same label. The length is the number of edges in that path.

Example:

A = [1, 1, 1, 2, 2]
E = [1, 2, 1, 3, 2, 4, 2, 5]

This tree is shown below. A node follows the form label, value.

----------1, 1

-----1, 2        1, 3

2, 4      2, 5
"""

def solution(A, E):
    dict =  {}
    i = 0
    while i < len(E)-1:
        if A[E[i]-1] == A[E[i+1]-1]:
            # print(E[i],E[i+1])
            # print(A[E[i]-1], A[E[i+1]-1])
            if A[E[i] - 1] in dict:
                dict[A[E[i] - 1]] += 1
            else:
                dict[A[E[i] - 1]] = 1
        i += 2
    print(dict)
    return  dict[max(dict, key=dict.get)]


A = [1, 1, 1, 2, 2, 1, 1, 2]
E = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8]
x = solution(A, E)
print(x)
