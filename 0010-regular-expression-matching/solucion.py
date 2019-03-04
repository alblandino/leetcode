class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] es True si s[i:] coincide con p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (p[j] == s[i] or p[j] == ".")

                if j + 1 < n and p[j + 1] == "*":
                    # x* usado cero veces, o consumir un caracter y seguir en el mismo x*
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


if __name__ == "__main__":
    s = Solution()

    assert s.isMatch("aa", "a") is False
    assert s.isMatch("aa", "a*") is True
    assert s.isMatch("ab", ".*") is True
    assert s.isMatch("aab", "c*a*b") is True
    assert s.isMatch("mississippi", "mis*is*p*.") is False
    assert s.isMatch("a", "ab*") is True
    assert s.isMatch("ab", ".*c") is False

    print("ok")
