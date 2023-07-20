from ctypes import py_object


class Array:
    def __init__(self, size):
        # FIXED size array from C language
        self.growth_factor = 2
        self.max_size = 16

        self.size = size
        self._capacity = max(self.max_size, self.growth_factor * size)

        array_data_type = py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index):
        return self.memory[index]

    def __setitem__(self, index, value):
        self.memory[index] = value

    def __str__(self) -> str:
        return self.memory

    def expand_capacity(self):
        self._capacity *= self.growth_factor
        array_data_type = py_object * (self._capacity)
        new_memory = array_data_type()

        for i in range(self.size):
            new_memory[i] = self.memory[i]

        del self.memory
        self.memory = new_memory

    def append(self, value):
        if self.size == self._capacity:
            self.expand_capacity()
        # # double original array size # (self.size + 1)
        # array_data_type = py_object * (self.size * self.growth_factor)
        # new_memory = array_data_type()

        # # copy items from original array to double size array
        # for i in range(self.size):
        #     new_memory[i] = self.memory[i]

        # add new item
        self.memory[self.size] = value

        # increment capacity
        self.size += 1

        # # delete old array
        # del self.memory

        # # reset old array to point to new array
        # self.memory = new_memory


if __name__ == '__main__':
    # array = Array(6)    # fixed array
    # print(f'array size : {len(array)}')

    # for i in range(array.size):  # set
    #     array.memory[i] = i+1

    # # for i in range(array.size):  # get
    # #     print(array.memory[i])

    # # del array.memory[0] # NOT support
    # # del array.memory     # Delete whole array
    # # in C++, corresponds to destroying whole array

    # array.append(7)

    # for i in range(array.size):  # get
    #     print(array.memory[i])
    array = Array(3)

    for i in range(array.size):  # set
        array.memory[i] = i+1

    array.append(12)
    array.append(4)

    for i in range(10**6):
        array.append(i)

    print(len(array))
