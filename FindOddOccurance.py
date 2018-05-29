"""
Programming Challenge Description:
Given a comma seperated set of integers, find and print the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Input:
Comma seperated integers. Example:
20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5
Output:
One integer. Example:
5
"""

def solution(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] %2 == 0:
            count.pop(num, None)

    for key in count:
        return key

nums = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

x = solution(nums)
print(x)



