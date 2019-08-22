class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # dp[col] = suma minima para llegar a (fila actual, col)
        dp = [0] * cols

        # primera fila: solo se llega desde la izquierda
        dp[0] = grid[0][0]
        for col in range(1, cols):
            dp[col] = dp[col - 1] + grid[0][col]

        for row in range(1, rows):
            # primera columna: solo se llega desde arriba
            dp[0] += grid[row][0]
            for col in range(1, cols):
                dp[col] = grid[row][col] + min(dp[col], dp[col - 1])

        return dp[cols - 1]


if __name__ == "__main__":
    s = Solution()

    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12

    assert s.minPathSum([[5]]) == 5
    assert s.minPathSum([[1, 2, 3]]) == 6
    assert s.minPathSum([[1], [2], [3]]) == 6
    assert s.minPathSum([[0, 9], [0, 0]]) == 0

    print("ok")
