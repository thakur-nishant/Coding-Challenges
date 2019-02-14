# Find closest repeating character/number in a list


def solution(coupons):
    # write your code in Python 3.6
    last_index = {}
    distance = {}
    for i in range(len(coupons)):
        num = coupons[i]
        if num in last_index:
            temp = i - last_index[num]
            if num in distance:
                if temp < distance[num]:
                    distance[num] = temp
            else:
                distance[num] = temp
        last_index[num] = i

    if distance:
        return distance[(min(distance, key=distance.get))] + 1   # extra one to buy coupons from start to end

    return -1


# coupons = [3,6,1,9]
coupons = [5, 3, 4, 2, 3, 4, 5, 7]
x = solution(coupons)
print(x)