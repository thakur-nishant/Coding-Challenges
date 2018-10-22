def solution(S):
    if not S:
        return 0
    max_count = 0
    char_count = {}

    for ch in S:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

        if char_count[ch] > max_count:
            max_count = char_count[ch]
            result = ch

    return result