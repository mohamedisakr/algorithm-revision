def numberOfSteps(num: int) -> int:
    # Time:   O(log(n))
    # Memory: O(1)
    steps = 0

    while num != 0:
        steps += 1
        # returns 1 if the least significant bit of num is 1,
        # which means num is odd.
        if num & 1:
            num -= 1
        else:
            # assigns num the value of num right shifted by one bit,
            # which means dividing by two
            num >>= 1

    return steps


'''
def numberOfSteps(num: int) -> int:
    # Time:   O(1)
    # Memory: O(1)
    # if num == 0:
    #     return 0
    # return num.bit_length() - 1 + num.bit_count()
'''

'''
    # ------- my solution -------
def numberOfSteps(num: int) -> int:    
    # Time:   O(n)
    # Memory: O(n)

    steps = 0
    while num != 0:
        steps += 1
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
            steps += 1

    return steps
'''
