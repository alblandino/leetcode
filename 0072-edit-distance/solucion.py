class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] = distancia entre word1[:i] y word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i  # borrar los i caracteres
        for j in range(n + 1):
            dp[0][j] = j  # insertar los j caracteres

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    replace = dp[i - 1][j - 1]
                    delete = dp[i - 1][j]
                    insert = dp[i][j - 1]
                    dp[i][j] = 1 + min(replace, delete, insert)

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()

    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5

    assert s.minDistance("", "") == 0
    assert s.minDistance("abc", "") == 3
    assert s.minDistance("", "ab") == 2
    assert s.minDistance("same", "same") == 0
    assert s.minDistance("a", "b") == 1

    print("ok")
