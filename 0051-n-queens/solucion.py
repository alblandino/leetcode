def build_board(queen_cols: list[int], n: int) -> list[str]:
    board = []
    for col in queen_cols:
        board.append("." * col + "Q" + "." * (n - col - 1))
    return board


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        queen_cols = []  # queen_cols[row] = columna de la reina en esa fila
        cols = set()
        diagonals = set()  # row - col es igual en toda la diagonal
        anti_diagonals = set()  # row + col es igual en toda la antidiagonal

        def place_row(row: int) -> None:
            if row == n:
                results.append(build_board(queen_cols, n))
                return

            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue

                queen_cols.append(col)
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                place_row(row + 1)

                # deshacer para probar la siguiente columna
                queen_cols.pop()
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        place_row(0)
        return results


def is_valid_board(board: list[str]) -> bool:
    # revisa que haya una reina por fila y que ninguna ataque a otra
    queens = []
    for row, line in enumerate(board):
        if line.count("Q") != 1:
            return False
        queens.append((row, line.index("Q")))

    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            r1, c1 = queens[i]
            r2, c2 = queens[j]
            if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                return False
    return True


if __name__ == "__main__":
    s = Solution()

    expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    assert sorted(s.solveNQueens(4)) == sorted(expected)
    assert s.solveNQueens(1) == [["Q"]]

    assert s.solveNQueens(2) == []
    assert s.solveNQueens(3) == []
    boards = s.solveNQueens(6)
    assert len(boards) == 4
    assert all(is_valid_board(board) for board in boards)
    assert len(s.solveNQueens(8)) == 92

    print("ok")
