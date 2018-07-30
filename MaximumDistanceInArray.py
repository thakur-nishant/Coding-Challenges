# def maxDifference(a):
#     if len(a) <= 1:
#         return -1
#     min_num = a[0]
#     result = -1
#     for num in a[1:]:
#         if num <= min_num:
#             min_num = num
#         else:
#             result = max(result, num - min_num)
#     return result

def maxDifference(a):
    min_elem = a[0]
    max_elem = a[0]
    max_diff = -1

    for elem in a[1:]:
        if elem < min_elem:
            min_elem =elem
            max_elem = elem
        if elem > max_elem:
            max_diff = max(max_diff, elem - min_elem)
            max_elem = elem

    return max_diff

a = [1, 2, 6, 80, 100]
# a = [-8,0,8]
# a = [2,2,2,2,2]
# a = [2,3,10,2,4,8,1]
# a = [5,4,3,2,1]
x = maxDifference(a)
print(x)
