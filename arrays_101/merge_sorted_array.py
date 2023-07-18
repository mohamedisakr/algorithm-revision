'''def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    [1,2,3,0,0,0]
    [2,5,6]
    """
    big = 0
    small = 0
    while big < m and small < n:
        if nums2[small] < nums1[big]:
            nums1[big], nums2[small] = nums2[small], nums1[big]
            small += 1
            big += 1
        else:
            big += 1
    # copy the remaining elements of nums2 to nums1
    while small < n:
        nums1[big] = nums2[small]
        big += 1
        small += 1
    print(nums1)
'''


def merge_2_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    [2,5,6]
    [1,2,3]
    """
    len_first = len(nums1)
    len_second = len(nums2)
    arr = []

    i = 0
    j = 0

    while i < len_first and j < len_second:
        if nums1[i] > nums2[j]:
            arr.append(nums2[j])
            j += 1
        else:
            arr.append(nums1[i])
            i += 1

    while i < len_first:
        arr.append(nums1[i])
        i += 1

    while j < len_second:
        arr.append(nums2[j])
        j += 1

    return arr


# nums_1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums_2 = [2, 5, 6]
# n = 3
# merge(nums_1, m, nums_2, n)

# i = n
# j = 0
# while i < m+n:
#     nums1[i] = nums2[j]
#     i += 1
#     j += 1
# print(nums1)
