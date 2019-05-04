class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # unico caso cuyo resultado no cabe en 32 bits
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        remaining = abs(dividend)
        base = abs(divisor)
        quotient = 0

        while remaining >= base:
            # duplicar el divisor mientras quepa en lo que queda
            chunk = base
            count = 1
            while chunk + chunk <= remaining:
                chunk += chunk
                count += count

            remaining -= chunk
            quotient += count

        if negative:
            return -quotient
        return quotient


if __name__ == "__main__":
    s = Solution()

    assert s.divide(10, 3) == 3
    assert s.divide(7, -3) == -2

    # desbordamiento: -2^31 / -1 se recorta a 2^31 - 1
    assert s.divide(-2147483648, -1) == 2147483647
    # extremos que si caben
    assert s.divide(-2147483648, 1) == -2147483648
    assert s.divide(2147483647, 2) == 1073741823
    # trunca hacia cero con negativos y divisor mas grande que el dividendo
    assert s.divide(-7, 2) == -3
    assert s.divide(1, 2) == 0
    assert s.divide(0, -5) == 0

    print("ok")
