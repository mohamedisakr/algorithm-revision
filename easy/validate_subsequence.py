def is_valid_subsequence(array: list[int], sequence: list[int]) -> bool:
    """Determines whether the second array is a subsequence of the first one.

    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

    Args:
        array (list[int]): The first array of integers.
        sequence (list[int]): The second array of integers.

    Returns:
        bool: True if sequence is a subsequence of array, False otherwise.

    Raises:
        TypeError: If either array or sequence is not a list or 
        contains non-integer elements.

    Example:
        >>> isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
        True
        >>> isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 26, 22])
        False        
        >>> isValidSubsequence([5, "a", 22], [5])
        TypeError: array and sequence must be lists of integers
    """

    if not all(isinstance(item, int) for item in array):
        raise TypeError("all elements in array must be of int data type")

    m = len(array)
    n = len(sequence)

    i = 0
    j = 0

    while i < m and j < n:
        if sequence[j] == array[i]:
            j += 1
        i += 1

    return j == n


'''
# case 1 -> true
array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, 10]
res = is_valid_subsequence(array1, sequence1)
print(f'is valid sub-sequence {res}')
print(res == True)

# case 2 -> false
array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [5, 26, 22]
res2 = is_valid_subsequence(array2, sequence2)
print(f'is valid sub-sequence {res2}')
print(res2 == True)

# Write your code here.
# for j in range(n):
#     for i in range(m):
#         if sequence[j] == array[i]:
#             count += 1
#             j += 1
#             i += 1
#             # return False
# print(f'# loop : {count}')
'''
