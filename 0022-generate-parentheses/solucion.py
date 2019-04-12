class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        current = []

        def backtrack(open_count, close_count):
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # se puede abrir mientras queden parentesis por usar
            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count)
                current.pop()

            # solo se cierra si hay alguno abierto sin cerrar
            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1)
                current.pop()

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.generateParenthesis(3)) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert s.generateParenthesis(1) == ["()"]
    assert sorted(s.generateParenthesis(2)) == ["(())", "()()"]
    assert len(s.generateParenthesis(4)) == 14
    assert len(set(s.generateParenthesis(8))) == 1430

    print("ok")
