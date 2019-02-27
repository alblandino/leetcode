class Solution:
    def isPalindrome(self, x: int) -> bool:
        # los negativos y los que terminan en 0 (salvo el 0) no pueden ser palindromos
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # cantidad par de digitos: mitades iguales
        # cantidad impar: se quita el digito del medio de reversed_half
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    s = Solution()

    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(0) is True
    assert s.isPalindrome(7) is True
    assert s.isPalindrome(1221) is True
    assert s.isPalindrome(1000021) is False

    print("ok")
