class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[col] = caminos para llegar a la casilla (fila actual, col)
        dp = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                # caminos desde arriba (valor viejo) + desde la izquierda
                dp[col] += dp[col - 1]

        return dp[n - 1]


if __name__ == "__main__":
    s = Solution()

    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3

    assert s.uniquePaths(1, 1) == 1
    assert s.uniquePaths(1, 10) == 1
    assert s.uniquePaths(3, 3) == 6
    assert s.uniquePaths(10, 10) == 48620

    print("ok")
