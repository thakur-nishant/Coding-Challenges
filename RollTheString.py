def rollTheString(s, roll):
    increment = [0] * len(s)
    a2z = [chr(i) for i in range(97, 97 + 26)]
    for num in roll:
        for i in range(num):
            increment[i] += 1
    result = ""
    for i in range(len(s)):
        index = ord(s[i]) + increment[i] - 97
        index = index % 26
        result += a2z[index]

    return result


# s = "vwxyz"
# roll = [1,2,3,4,5]

s = "abz"
roll = [3,2,1]

x = rollTheString(s,roll)
print(x)
