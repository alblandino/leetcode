class Solution:
    def isValid(self, s: str) -> bool:
        # cierre -> apertura que le corresponde
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        # si quedo algo abierto, no esta balanceada
        return not stack


if __name__ == "__main__":
    s = Solution()

    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([])") is True
    assert s.isValid("([)]") is False
    assert s.isValid("(") is False
    assert s.isValid(")") is False
    assert s.isValid("{[]}") is True

    print("ok")
