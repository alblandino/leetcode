class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # modifica matrix en el lugar, no devuelve nada
        rows, cols = len(matrix), len(matrix[0])

        first_row_has_zero = False
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True

        first_col_has_zero = False
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True

        # la primera fila y la primera columna guardan las marcas
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # se limpian al final para no borrar las marcas antes de usarlas
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0


if __name__ == "__main__":
    s = Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert s.setZeroes(matrix) is None
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    matrix = [[1]]
    s.setZeroes(matrix)
    assert matrix == [[1]]

    matrix = [[1, 0]]
    s.setZeroes(matrix)
    assert matrix == [[0, 0]]

    matrix = [[1], [0]]
    s.setZeroes(matrix)
    assert matrix == [[0], [0]]

    matrix = [[1, 1, 1], [0, 1, 2]]
    s.setZeroes(matrix)
    assert matrix == [[0, 1, 1], [0, 0, 0]]

    print("ok")
