class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        best_length = 0

        for center in range(len(s)):
            # centro en un caracter (largo impar) y entre dos caracteres (largo par)
            for left, right in ((center, center), (center, center + 1)):
                start, length = self.expand(s, left, right)
                if length > best_length:
                    best_start = start
                    best_length = length

        return s[best_start:best_start + best_length]

    def expand(self, s: str, left: int, right: int) -> tuple[int, int]:
        # abre hacia los lados mientras los extremos coincidan
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # al salir, left y right quedaron una posicion afuera del palindromo
        return left + 1, right - left - 1


if __name__ == "__main__":
    s = Solution()

    assert s.longestPalindrome("babad") in ("bab", "aba")
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("ac") in ("a", "c")
    assert s.longestPalindrome("racecar") == "racecar"
    assert s.longestPalindrome("forgeeksskeegfor") == "geeksskeeg"

    print("ok")
