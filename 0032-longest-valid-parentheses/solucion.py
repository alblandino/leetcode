class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # el fondo de la pila es el indice justo antes del tramo valido actual
        stack = [-1]
        best = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # este ')' no tiene pareja, pasa a ser el nuevo borde
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])

        return best


if __name__ == "__main__":
    s = Solution()

    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses("") == 0

    # sin ningun par valido
    assert s.longestValidParentheses("))((") == 0
    # pares anidados y seguidos forman un solo tramo
    assert s.longestValidParentheses("()(())") == 6
    # un '(' sin cerrar parte la cadena en dos tramos
    assert s.longestValidParentheses("()(()") == 2

    print("ok")
