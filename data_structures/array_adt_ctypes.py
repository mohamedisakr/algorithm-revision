from ctypes import py_object


class Array:
    def __init__(self, size=0):
        # current position
        # self.pos = 0

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
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result

    def expand_capacity(self):
        self._capacity *= self.growth_factor
        array_data_type = py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):
            new_memory[i] = self.memory[i]

        del self.memory
        self.memory = new_memory

    def append(self, item):
        if self.size == self._capacity:
            self.expand_capacity()

        self.memory[self.size] = item

        # increment capacity
        self.size += 1

    def insert(self, index, value):
        assert 0 <= index < self.size

        if self.size == self._capacity:
            self.expand_capacity()

        # shift all items 1 unit to the right
        # shift from the end of array
        for i in range(self.size-1, index-1, -1):
            self.memory[i+1] = self.memory[i]

        self.memory[index] = value
        self.size += 1

    def pop(self, index):
        assert 0 <= index < self.size
        for i in range(self.size-1, index, -1):
            self.memory[i-1] = self.memory[i]
        self.size -= 1


if __name__ == '__main__':
    '''
    array = Array()

    array.append(56)
    array.append('hello')
    array.insert(0, 'A0')

    print(array)

    array.insert(2, 'A2')
    print(array)

    array.insert(1, 4)
    print(array)
    '''

    # pop
    array = Array()
    array.append(10)
    array.append(20)
    array.append(30)
    array.append(40)
    print(array)

    array.pop(2)
    print(array)
