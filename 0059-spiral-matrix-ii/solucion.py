class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        value = 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                matrix[top][col] = value
                value += 1
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right] = value
                value += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = value
                    value += 1
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = value
                    value += 1
                left += 1

        return matrix


if __name__ == "__main__":
    s = Solution()

    assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert s.generateMatrix(1) == [[1]]

    assert s.generateMatrix(2) == [[1, 2], [4, 3]]
    assert s.generateMatrix(4) == [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]

    print("ok")
