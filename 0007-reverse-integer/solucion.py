class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # se revisa antes de multiplicar para no salirse nunca del rango
            if result > (INT_MAX - digit) // 10:
                return 0
            result = result * 10 + digit

        return sign * result


if __name__ == "__main__":
    s = Solution()

    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(0) == 0
    assert s.reverse(1534236469) == 0
    assert s.reverse(-2147483648) == 0
    assert s.reverse(1463847412) == 2147483641

    print("ok")
