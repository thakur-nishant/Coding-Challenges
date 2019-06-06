def orderJunctionBoxes(numberOfBoxes, boxList):
    if not boxList:
        return []
    log_old = []
    log_new = []
    for box in boxList:
        idx = box.index(" ")
        key = box[:idx]
        value = box[idx + 1:]
        if value[0].isdigit():
            log_new.append(box)
        else:
            log_old.append([key,value])

    sorted_log = sorted(log_old, key=lambda x: (x[1], x[0]))
    final = [" ".join(each) for each in sorted_log]
    return final+log_new


boxList = [
    "ykc 82 01",
    "ykc 83 01",
    "eo first qpx",
    "09z cat hamster",
    "09z dog hamster",
    "06f 12 25 6",
    "az0 first qpx",
    "236 cat dog rabbit snake"
]

print(orderJunctionBoxes(len(boxList), boxList))
