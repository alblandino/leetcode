class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            # la posicion mid de la lista "aplanada" es esta celda
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True
            if value < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    s = Solution()

    grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(grid, 3) is True
    assert s.searchMatrix(grid, 13) is False

    assert s.searchMatrix([[1]], 1) is True
    assert s.searchMatrix([[1]], 2) is False
    assert s.searchMatrix([[1], [3]], 3) is True
    assert s.searchMatrix(grid, 0) is False
    assert s.searchMatrix(grid, 60) is True
    assert s.searchMatrix(grid, 61) is False

    print("ok")
