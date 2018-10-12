def budgetShopping(W, val, wt):
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    n = len(val)
    dp = [0 for i in range(W + 1)]

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[W]

test1 = budgetShopping(4,[10],[2])
# test1 = budgetShopping(50,[20,19],[24,20])
print(test1)