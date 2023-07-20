from array import array


class MyArray:

    def __init__(self, size):
        self.capacity = 0
        self.size = size
        self.items = array('i', [0 for item in range(size)])

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.capacity += 1
        self.items[index] = value

    def __str__(self) -> str:
        pass
        # return [item for item in range(self.size)].join(',')  # .tolist()
        # return self.items  # .tolist()

    def append(self, item):
        # print(f'size : {self.size}')
        # print(f'capacity : {self.capacity}')
        if self.size == self.capacity:
            # double original array size
            # copy items from original array to double size array
            # add new item
            # increment capacity
            pass


if __name__ == '__main__':
    array = MyArray(6)
    print(f'array size : {len(array)}')

    for i in range(array.size):  # set
        array.items[i] = i+1

    for i in range(array.size):  # get
        print(array.items[i])

    # array.append(7)

    print(f'items : {array.items}')
    print(f'array capacity : {array.capacity}')

    # del array.items[0] # NOT support
    # del array.items     # Delete whole array
    # in C++, corresponds to destroying whole array
