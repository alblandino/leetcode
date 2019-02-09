class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # caracter -> ultima posicion donde aparecio
        last_seen = {}
        start = 0
        best = 0

        for i, char in enumerate(s):
            # si el caracter esta repetido dentro de la ventana, el inicio salta despues de el
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1

            last_seen[char] = i
            best = max(best, i - start + 1)

        return best


if __name__ == "__main__":
    s = Solution()

    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring(" ") == 1
    assert s.lengthOfLongestSubstring("abba") == 2
    assert s.lengthOfLongestSubstring("dvdf") == 3

    print("ok")
