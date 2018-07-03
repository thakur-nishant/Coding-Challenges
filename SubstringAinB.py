"""
Given a string A consisting of n characters and a string B consisting of m characters, write a function that will return the number of times A must be stated such that B is a substring of the repeated A. If B can never be a substring, return -1.

Example:
A = ‘abcd’
B = ‘cdabcdab’
The function should return 3 because after stating A 3 times, getting ‘abcdabcdabcd’, B is now a substring of A.

You can assume that n and m are integers in the range [1, 1000].
"""

def solution(A,B):
    count = 1
    if (set(A) != set(B)) or not (A in B or B in A):
        return -1
    S = A
    check = len(B)//len(A) + 2
    while check:
        if B in S:
            return count
        else:
            S = S + A
            count += 1
        check -= 1
    return -1

A = "abcd"
B = "cdabcdab"

x = solution(A,B)
print(x)
