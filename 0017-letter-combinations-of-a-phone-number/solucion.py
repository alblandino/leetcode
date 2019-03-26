PHONE = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        result = []
        current = []

        def backtrack(index):
            if index == len(digits):
                result.append("".join(current))
                return

            for letter in PHONE[digits[index]]:
                current.append(letter)
                backtrack(index + 1)
                current.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.letterCombinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(s.letterCombinations("2")) == ["a", "b", "c"]
    assert sorted(s.letterCombinations("7")) == ["p", "q", "r", "s"]
    assert len(s.letterCombinations("79")) == 16
    assert len(s.letterCombinations("2345")) == 81

    print("ok")
