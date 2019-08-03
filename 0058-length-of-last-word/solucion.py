class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # saltar los espacios del final
        while i >= 0 and s[i] == " ":
            i -= 1

        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


if __name__ == "__main__":
    s = Solution()

    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6

    assert s.lengthOfLastWord("a") == 1
    assert s.lengthOfLastWord("day   ") == 3
    assert s.lengthOfLastWord("   hello") == 5

    print("ok")
