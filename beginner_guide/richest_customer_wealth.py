def maximumWealth(accounts: list[list[int]]) -> int:
    return max(map(sum, accounts))

    # return max(sum(acc) for acc in accounts)

    # richest = 0
    # for customer in accounts:
    #     total = 0
    #     for balance in customer:
    #         total += balance
    #     richest = max(total, richest)

    # return richest
