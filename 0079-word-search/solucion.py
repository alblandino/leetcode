from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        # poda: si al tablero le faltan letras, no hace falta buscar
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        for ch, count in word_count.items():
            if board_count[ch] < count:
                return False

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[index]:
                return False

            # se marca la celda como usada mientras se explora este camino
            saved = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )
            board[r][c] = saved
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert s.exist(board, "ABCCED") is True
    assert s.exist(board, "SEE") is True
    assert s.exist(board, "ABCB") is False
    # el tablero queda igual despues de buscar
    assert board == [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    assert s.exist([["a"]], "a") is True
    assert s.exist([["a", "b"], ["c", "d"]], "abdc") is True
    assert s.exist([["a", "b"], ["c", "d"]], "abcd") is False
    assert s.exist([["a", "a"]], "aaa") is False

    print("ok")
