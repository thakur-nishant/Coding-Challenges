def solution(total_money, total_damage, costs, damages):
    # write your code in Python 3.6

    greedy1 = []
    for i, cost in enumerate(costs):
        greedy1.append([damages[i] / cost, cost, damages[i]])

    greedy1.sort(reverse=True, key=lambda x: x[0])

    for key in greedy1:

        temp_cost = key[1]
        temp_dmg = key[2]
        if (total_money - temp_cost >= 0):
            total_damage -= temp_dmg
            total_money -= temp_cost

        if (total_damage <= 0):
            return True

    if (total_damage <= 0):
        return True
    else:
        return False

x = solution(5,5,[1,2,5],[2,1,3])
print(x)
