VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            value = VALUES[s[i]]
            # si el de la derecha es mayor, este simbolo resta (IV, IX, XL, ...)
            if i + 1 < len(s) and value < VALUES[s[i + 1]]:
                total -= value
            else:
                total += value

        return total


if __name__ == "__main__":
    s = Solution()

    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("I") == 1
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("MMMCMXCIX") == 3999

    print("ok")
