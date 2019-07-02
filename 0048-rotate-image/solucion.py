class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 1. transponer: las filas pasan a ser columnas
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. invertir cada fila
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    s = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # matriz de 1 x 1
    matrix = [[-1000]]
    s.rotate(matrix)
    assert matrix == [[-1000]]

    # matriz de 2 x 2, y cuatro giros la dejan como estaba
    matrix = [[1, 2], [3, 4]]
    s.rotate(matrix)
    assert matrix == [[3, 1], [4, 2]]
    s.rotate(matrix)
    s.rotate(matrix)
    s.rotate(matrix)
    assert matrix == [[1, 2], [3, 4]]

    print("ok")
