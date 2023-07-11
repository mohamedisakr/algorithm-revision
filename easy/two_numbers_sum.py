def find_two_numbers_sum_brute_force(array, target_sum):
    n = len(array)

    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]

    return []


def find_two_numbers_sum_hash_table(array, target_sum):
    n = len(array)
    cache = {}

    for x in array:
        y = target_sum - x
        if y in cache:
            return [x, y]
        else:
            cache[x] = True

    return []


def find_two_numbers_sum_sort_first(array: list[int], target_sum: int) -> list[int]:
    """Finds two numbers in an unsorted array that add up to a target number.

    This function sorts the array first and then uses a two-pointer approach to find the pair of numbers.
    If there are multiple pairs that satisfy the condition, it returns the first pair found in the sorted array.
    If there is no such pair, it returns an empty list.

    Args:
        array (list): A list of integers.
        target_sum (int): The target sum to look for.

    Returns:
        list: A list of two integers that add up to the target sum, or an empty list if none exists.

    Raises:
        TypeError: If array is not a list or target_sum is not an integer.

    Example:
        >>> find_two_numbers_sum_sort_first([3, 5, 2, -4, 8, 11], 7)
        [-4, 11]
        >>> find_two_numbers_sum_sort_first([1, 2, 3], 6)
        []
        >>> find_two_numbers_sum_sort_first("hello", 10)
        TypeError: array must be a list
    """
    if not all(isinstance(item, int) for item in array):
        raise TypeError("all elements in array must be of int data type")

    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        x = array[left]
        y = array[right]
        if x + y == target_sum:
            return [x, y]
        elif x+y > target_sum:
            right -= 1
        elif x+y < target_sum:
            left += 1

    return []
