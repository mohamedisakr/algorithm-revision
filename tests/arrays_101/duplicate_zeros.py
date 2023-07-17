from datetime import date


def insert(arr,  i,  j):
    if j < len(arr):
        arr[j] = arr[i]


def duplicateZeros(arr: list[int]) -> None:
    if arr is None or len(arr) == 0:
        return

    n = len(arr)
    zeros = arr.count(0)

    i = n - 1
    j = n + zeros - 1

    while i != j:
        insert(arr, i, j)
        j -= 1
        if (arr[i] == 0):
            insert(arr, i, j)
            j -= 1
        i -= 1


arr1 = [1, 0, 2]
duplicateZeros(arr1)

arr2 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr2)

# actual = duplicateZeros(arr1)
# expected = [1, 0, 0]
# assert actual == expected

# ------------ append to front ---------------------
# arr = [1, 2, 3, 4, 5, 6, 7]
# arr = [8]+arr
# print(arr)
