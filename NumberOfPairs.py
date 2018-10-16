def numberOfPairs(a, k):
    history = {}
    result = set()
    for num in a:
        if num in history:
            result.add(tuple(sorted([num,history[num]])))
        else:
            history[num] = k - num

    return len(result)


a = [1,3,46,1,3,9]
k = 47

test = numberOfPairs(a, k)
print(test)
