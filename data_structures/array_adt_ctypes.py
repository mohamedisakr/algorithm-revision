from ctypes import py_object


class Array:

    def __init__(self, size):
        self.capacity = 0

        # FIXED size array from C language
        array_data_type = py_object * size
        self.size = size
        self.memory = array_data_type()

        for i in range(size):
            self.memory[i] = None

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index):
        return self.memory[index]

    def __setitem__(self, index, value):
        self.capacity += 1
        self.memory[index] = value

    def __str__(self) -> str:
        return self.memory

    def append(self, item):
        # double original array size
        array_data_type = py_object * (self.size + 1)
        new_memory = array_data_type()

        # copy items from original array to double size array
        for i in range(self.size):
            new_memory[i] = self.memory[i]

        # add new item
        new_memory[self.size] = item

        # increment capacity
        self.size += 1

        # delete old array
        del self.memory

        # reset old array to point to new array
        self.memory = new_memory


if __name__ == '__main__':
    array = Array(6)    # fixed array
    print(f'array size : {len(array)}')

    # TODO:  printing all array items
    # print(f'items : {array}')

    for i in range(array.size):  # set
        array.memory[i] = i+1

    # for i in range(array.size):  # get
    #     print(array.memory[i])

    # del array.memory[0] # NOT support
    # del array.memory     # Delete whole array
    # in C++, corresponds to destroying whole array

    array.append(7)

    for i in range(array.size):  # get
        print(array.memory[i])
