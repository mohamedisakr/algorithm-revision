def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    last = (m + n) - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            last -= 1
            i -= 1
        else:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1
    print(nums1)


def merge_2_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
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
