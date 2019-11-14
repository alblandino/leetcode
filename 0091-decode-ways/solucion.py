class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = formas de decodificar los primeros i digitos
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # el ultimo digito solo (1 a 9)
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            # los dos ultimos digitos juntos (10 a 26)
            if i >= 2:
                two_digits = int(s[i - 2:i])
                if 10 <= two_digits <= 26:
                    dp[i] += dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    s = Solution()

    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
    assert s.numDecodings("06") == 0
    assert s.numDecodings("0") == 0
    assert s.numDecodings("10") == 1
    assert s.numDecodings("100") == 0
    assert s.numDecodings("27") == 1
    assert s.numDecodings("11106") == 2

    print("ok")
