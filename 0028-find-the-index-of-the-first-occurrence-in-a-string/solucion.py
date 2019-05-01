class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # solo se prueban los inicios donde needle todavia cabe
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1

    # needle mas largo que haystack
    assert s.strStr("abc", "abcd") == -1
    # coincidencia al final
    assert s.strStr("hello", "llo") == 2
    # cadenas iguales
    assert s.strStr("a", "a") == 0

    print("ok")
