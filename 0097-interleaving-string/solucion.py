class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        # dp[i][j] = se puede formar s3[:i + j] con s1[:i] y s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                # el ultimo caracter de s3[:i + j] viene de s1
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                # o viene de s2
                if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()

    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert s.isInterleave("", "", "") is True
    assert s.isInterleave("", "", "a") is False
    assert s.isInterleave("a", "", "a") is True
    assert s.isInterleave("", "b", "b") is True
    assert s.isInterleave("ab", "cd", "acbd") is True
    assert s.isInterleave("ab", "cd", "adbc") is False

    print("ok")
