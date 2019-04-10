def minNum(threshold, happy):
    queue = []

    visited =set()
    queue.append((1,0,happy[0], happy[0]))

    while queue:
        res, pos, max_score, min_score = queue.pop(0)
        visited.add((res, pos, max_score, min_score))
        if max_score - min_score >= threshold:
            return res
        if pos+1 < len(happy) and (res+1, pos+1, max(max_score, happy[pos+1]), min(min_score, happy[pos+1])) not in visited:
            queue.append((res+1, pos+1, max(max_score, happy[pos+1]), min(min_score, happy[pos+1])))
        if pos+2 < len(happy) and (res+1, pos+2, max(max_score, happy[pos+2]), min(min_score, happy[pos+2])) not in visited:
            queue.append((res+1, pos+2, max(max_score, happy[pos+2]), min(min_score, happy[pos+2])))
    return 0


# threshold = 4
# happy = [1,2,3,4,5]
threshold = 4
happy = [1,3,4,7]
print(minNum(threshold,happy))
