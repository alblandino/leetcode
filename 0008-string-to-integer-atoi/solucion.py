class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        n = len(s)
        i = 0

        # 1. espacios del inicio
        while i < n and s[i] == " ":
            i += 1

        # 2. signo opcional
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. digitos, convertidos a mano
        result = 0
        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            result = result * 10 + digit

            # 4. recortar apenas se sale del rango
            if sign * result > INT_MAX:
                return INT_MAX
            if sign * result < INT_MIN:
                return INT_MIN
            i += 1

        return sign * result


if __name__ == "__main__":
    s = Solution()

    assert s.myAtoi("42") == 42
    assert s.myAtoi(" -042") == -42
    assert s.myAtoi("1337c0d3") == 1337
    assert s.myAtoi("0-1") == 0
    assert s.myAtoi("words and 987") == 0
    assert s.myAtoi("") == 0
    assert s.myAtoi("-91283472332") == -2147483648
    assert s.myAtoi("2147483648") == 2147483647
    assert s.myAtoi("+-12") == 0
    assert s.myAtoi("   +0 123") == 0

    print("ok")
