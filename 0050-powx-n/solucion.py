class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        # exponenciacion rapida: x se eleva al cuadrado y n se parte a la mitad
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result


def is_close(a: float, b: float) -> bool:
    return abs(a - b) < 1e-5


if __name__ == "__main__":
    s = Solution()

    assert is_close(s.myPow(2.0, 10), 1024.0)
    assert is_close(s.myPow(2.1, 3), 9.261)
    assert is_close(s.myPow(2.0, -2), 0.25)

    # exponente cero
    assert is_close(s.myPow(5.0, 0), 1.0)
    # base negativa con exponente impar
    assert is_close(s.myPow(-2.0, 3), -8.0)
    # exponentes extremos
    assert is_close(s.myPow(1.0, -2147483648), 1.0)
    assert is_close(s.myPow(-1.0, 2147483647), -1.0)

    print("ok")
