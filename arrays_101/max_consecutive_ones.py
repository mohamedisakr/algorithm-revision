def findMaxConsecutiveOnes(nums: list[int]) -> int:
    n = len(nums)
    max_count = 0
    count = 0
    mask = 0  # bit mask that helps to check if the current element is one or zero

    for i in range(n):
        if nums[i] == 1:
            # shifts the mask one bit to the left and sets the rightmost bit
            # to one using the bitwise or operator (|)
            mask = (mask << 1) | 1
        else:
            # shifts the mask one bit to the left and sets the rightmost bit
            # to zero
            mask = mask << 1

        # checks if the element and the mask have any common bits using
        # the bitwise and operator (&).
        if (nums[i] & mask) != 0:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
            mask = 0

    return max(max_count, count)

    # n = len(nums)
    # count = 0
    # max_ones = 0

    # for i in range(0, n):
    #     # Reset count when 0 is found
    #     if (nums[i] == 0):
    #         count = 0

    #     # If 1 increment count and update max ones
    #     else:
    #         count += 1
    #         max_ones = max(max_ones, count)

    # return max_ones


nums1 = [1, 1, 0, 1, 1, 1]
actual = findMaxConsecutiveOnes(nums1)
print(f'actual : {actual}')
expected = 3
print(actual == expected)
