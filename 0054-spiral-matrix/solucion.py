class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # si queda una sola fila o columna, no volver por el mismo camino
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7
    ]

    assert s.spiralOrder([[7]]) == [7]
    assert s.spiralOrder([[1, 2, 3]]) == [1, 2, 3]
    assert s.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert s.spiralOrder([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]

    print("ok")
