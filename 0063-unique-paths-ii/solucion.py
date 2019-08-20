class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid[0])
        # dp[col] = caminos hasta la casilla (fila actual, col)
        dp = [0] * n
        dp[0] = 1

        for row in obstacleGrid:
            for col in range(n):
                if row[col] == 1:
                    dp[col] = 0
                elif col > 0:
                    # dp[col] todavia tiene el valor de la fila de arriba
                    dp[col] += dp[col - 1]

        return dp[n - 1]


if __name__ == "__main__":
    s = Solution()

    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1

    assert s.uniquePathsWithObstacles([[0]]) == 1
    assert s.uniquePathsWithObstacles([[1]]) == 0
    assert s.uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0
    assert s.uniquePathsWithObstacles([[0], [1], [0]]) == 0
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0]]) == 3

    print("ok")
