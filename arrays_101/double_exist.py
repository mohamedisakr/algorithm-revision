def checkIfExist(arr: list[int]) -> bool:
    n = len(arr)

    if n == 0:
        return False

    store = set()

    for item in arr:
        if item * 2 in store or item / 2 in store:
            return True
        store.add(item)

    return False
