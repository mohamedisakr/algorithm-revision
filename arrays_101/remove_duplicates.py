def removeDuplicates(nums: list[int]) -> int:
    next_valid = 1
    i = 1
    n = len(nums)

    while i < n:
        if nums[next_valid-1] != nums[i]:
            nums[next_valid] = nums[i]
            next_valid += 1
        i += 1

    return next_valid
