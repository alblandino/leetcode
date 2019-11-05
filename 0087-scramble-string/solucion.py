class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # memo[(i, j, length)] dice si s1[i:i+length] se puede revolver en s2[j:j+length]
        memo = {}

        def check(i: int, j: int, length: int) -> bool:
            key = (i, j, length)
            if key in memo:
                return memo[key]

            part1 = s1[i:i + length]
            part2 = s2[j:j + length]
            if part1 == part2:
                memo[key] = True
                return True
            # si no tienen las mismas letras es imposible
            if sorted(part1) != sorted(part2):
                memo[key] = False
                return False

            result = False
            for k in range(1, length):
                # sin intercambio: inicio con inicio y final con final
                if check(i, j, k) and check(i + k, j + k, length - k):
                    result = True
                    break
                # con intercambio: el inicio de s1 va al final de s2
                if check(i, j + length - k, k) and check(i + k, j, length - k):
                    result = True
                    break

            memo[key] = result
            return result

        return check(0, 0, len(s1))


if __name__ == "__main__":
    s = Solution()

    assert s.isScramble("great", "rgeat") is True
    assert s.isScramble("abcde", "caebd") is False
    assert s.isScramble("a", "a") is True
    assert s.isScramble("ab", "ba") is True
    assert s.isScramble("abc", "bca") is True
    assert s.isScramble("abcd", "bdac") is False
    assert s.isScramble("aa", "ab") is False

    print("ok")
