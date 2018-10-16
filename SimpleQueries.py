def counts(nums, maxes):
    nums = sorted(nums)
    maxes = sorted(maxes)
    result = []

    num_idx = mx_idx = 0
    while num_idx < len(nums) and mx_idx < len(maxes):
        if maxes[mx_idx] >= nums[num_idx]:
            num_idx += 1
        else:
            result.append(num_idx)
            mx_idx += 1

    while mx_idx < len(maxes):
        result.append(len(nums))
        mx_idx += 1

    return result


# nums = [2,10,5,4,8]
# maxes = [3,1,7,8]
nums = [1,4,2,4]
maxes = [3,5]

test = counts(nums, maxes)
print(test)
