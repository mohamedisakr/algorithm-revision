from data_structures.array_adt_ctypes import Array


class Array2D:
    def __init__(self, rows, cols, initial_value=None):
        self.rows = rows
        self.cols = cols

        self.grid = Array(rows)
        for i in range(rows):
            self.grid[i] = Array(cols)  # , initial_value

    def __getitem__(self, index):
        r, c = index[0], index[1]
        return self.grid[r][c]

    def __setitem__(self, index, value):
        r, c = index[0], index[1]
        self.grid[r][c] = value

    def __str__(self) -> str:
        result = ''
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.grid[i][j]) + ', '
        return result
