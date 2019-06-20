class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] indica si s[:i] encaja con p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # con el texto vacio solo encajan los '*' del inicio
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # '*' vacio o '*' que cubre un caracter mas de s
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()

    assert s.isMatch("aa", "a") is False
    assert s.isMatch("aa", "*") is True
    assert s.isMatch("cb", "?a") is False

    # texto y patron vacios
    assert s.isMatch("", "") is True
    assert s.isMatch("", "***") is True
    assert s.isMatch("abc", "") is False
    # varios '*' que tienen que repartirse el texto
    assert s.isMatch("adceb", "*a*b") is True
    assert s.isMatch("acdcb", "a*c?b") is False

    print("ok")
