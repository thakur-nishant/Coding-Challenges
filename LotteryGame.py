# Find closest repeating character/number in a list

def solution(coupons):
    # write your code in Python 3.6
    last_index = {}
    distance = {}
    for i in range(len(coupons)):
        num = coupons[i]
        if num in last_index:
            temp = i - last_index[num]
            if num in distance and temp < distance[num]:
                distance[num] = temp
            else:
                distance[num] = temp




coupons = [5, 3, 4, 2, 3, 4, 5, 7]
x = solution(coupons)