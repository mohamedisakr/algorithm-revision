def sort(arr: list[int]) -> list[int]:
    n = len(arr)

    if n == 0 or n == 1:
        return arr

    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


a = [3, 2, 5, 9, 8, 1]
res = sort(a)
print(res)
