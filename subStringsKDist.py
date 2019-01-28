def subStringsKDist(inputStr, num):
    # WRITE YOUR CODE HERE
    if num == 0:
        return []
    result = set()
    for i in range(len(inputStr)-num+1):
        subStr = set(inputStr[i:i+num])
        if len(subStr) == num:
            result.add(inputStr[i:i+num])
    print(result)
    return result

print(subStringsKDist("abcd", 3))
