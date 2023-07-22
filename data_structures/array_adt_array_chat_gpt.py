# import the array module
from array import array


class Array:
    def __init__(self, size):
        # initialize an empty array of given size
        self.data = array('i', [0] * size)
        # keep track of the number of elements in the array
        self.length = 0

    def __len__(self):
        # return the length of the array
        return self.length

    def __getitem__(self, index):
        # check if the index is valid
        if 0 <= index < self.length:
            # return the element at the given index
            return self.data[index]
        else:
            # raise an exception if the index is out of bounds
            raise IndexError("Array index out of range")

    def __setitem__(self, index, value):
        # check if the index is valid
        if 0 <= index < self.length:
            # set the element at the given index to the given value
            self.data[index] = value
        else:
            # raise an exception if the index is out of bounds
            raise IndexError("Array index out of range")

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be of int data type")

        # check if there is enough space in the array
        if self.length < len(self.data):
            # add the value to the end of the array
            self.data[self.length] = value
            # increment the length of the array
            self.length += 1
        else:
            # raise an exception if the array is full
            raise OverflowError("Array is full")

    def insert(self, index, value):
        if not isinstance(value, int):
            raise TypeError("value must be of int data type")

        # check if the index is valid
        if 0 <= index <= self.length:
            # check if there is enough space in the array
            if self.length < len(self.data):
                # shift the elements from the index to the right by one position
                for i in range(self.length, index, -1):
                    self.data[i] = self.data[i-1]
                # insert the value at the given index
                self.data[index] = value
                # increment the length of the array
                self.length += 1
            else:
                # raise an exception if the array is full
                raise OverflowError("Array is full")
        else:
            # raise an exception if the index is out of bounds
            raise IndexError("Array index out of range")

    def remove(self, index):
        # check if the index is valid
        if 0 <= index < self.length:
            # store the element at the given index
            value = self.data[index]
            # shift the elements from the index to the left by one position
            for i in range(index, self.length-1):
                self.data[i] = self.data[i+1]
            # set the last element to None
            self.data[self.length-1] = 0  # None
            # decrement the length of the array
            self.length -= 1
            # return the removed element
            return value
        else:
            # raise an exception if the index is out of bounds
            raise IndexError("Array index out of range")


# # import the array module

# # create an array of integers
# a = array('i', [1, 2, 3])

# # try to append a non-integer value
# a.append("a")
