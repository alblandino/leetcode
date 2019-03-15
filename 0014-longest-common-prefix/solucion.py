class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            char = first[i]
            for word in strs[1:]:
                # la palabra se termino o tiene otra letra en esta posicion
                if i == len(word) or word[i] != char:
                    return first[:i]

        return first


if __name__ == "__main__":
    s = Solution()

    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["a"]) == "a"
    assert s.longestCommonPrefix(["", "b"]) == ""
    assert s.longestCommonPrefix(["ab", "a"]) == "a"
    assert s.longestCommonPrefix(["abc", "abc"]) == "abc"

    print("ok")
