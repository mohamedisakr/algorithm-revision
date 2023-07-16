from math import floor, log10


def has_even_digits(num):
    digits = 0
    try:
        log_10 = log10(num)
        digits = floor(log_10) + 1
    except ValueError:
        print(f'{num} must be positive integer')
    return digits % 2 == 0


def findNumbers(nums: list[int]) -> int:
    evens = 0
    for num in nums:
        try:
            log_10 = log10(num)
            digits = floor(log_10) + 1
            if digits % 2 == 0:  # has_even_digits(num) is True:  #
                evens += 1
        except ValueError:
            print(f'{num} must be positive integer')
    return evens


# def findNumbers(nums: list[int]) -> int:
#     def has_even_digits(num):
#         digits = len(str(num))
#         return digits % 2 == 0

#     return len([num for num in nums if has_even_digits(num)])
