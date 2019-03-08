# valores de mayor a menor, incluyendo las formas de resta
SYMBOLS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []

        for value, symbol in SYMBOLS:
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)


if __name__ == "__main__":
    s = Solution()

    assert s.intToRoman(3749) == "MMMDCCXLIX"
    assert s.intToRoman(58) == "LVIII"
    assert s.intToRoman(1994) == "MCMXCIV"
    assert s.intToRoman(1) == "I"
    assert s.intToRoman(4) == "IV"
    assert s.intToRoman(3999) == "MMMCMXCIX"

    print("ok")
