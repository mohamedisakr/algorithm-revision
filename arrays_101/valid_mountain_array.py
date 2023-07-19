def validMountainArray(arr: list[int]) -> bool:
    # TODO: revisit algorithm
    n = len(arr)

    if n == 0:
        return True

    if n == 2:
        if arr[0] > arr[1]:
            return 0
        else:
            return 1

    lo = 0
    hi = n

    while lo < n:
        m = lo + (hi-lo) // 2
        # m = (hi+lo) // 2
        if arr[m-1] > arr[m]:
            hi = m-1
        elif arr[m+1] > arr[m]:
            lo = m+1
        else:
            return True
    return False

    # lo = 0
    # hi = len(arr)

    # while lo < hi:
    #     m = lo + (hi-lo) // 2
    #     if arr[m] < arr[m-1]:
    #         hi = m-1
    #     elif arr[m] < arr[m+1]:
    #         lo = m+1
    #     else:
    #         return True  # arr[m]

    # return False
