class Matrix(list):
    def __matmul__(self, b):
        return Matrix([[sum((x * y) for x, y in zip(s_row, b_col)) for b_col in zip(*b)] for s_row in self])

    def __pow__(self, b):
        if b <= 1:
            return self
        temp = self ** (b // 2)
        if b % 2:
            return temp @ temp @ self
        return temp @ temp
