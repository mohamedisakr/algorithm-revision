def runningSum(nums: list[int]) -> list[int]:
    cumulative_sum = []
    total = 0
    for item in nums:
        total += item
        cumulative_sum.append(total)
    return cumulative_sum
