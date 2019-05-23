class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                # numero de caja 3x3, de 0 a 8 leyendo por filas
                box = (r // 3) * 3 + c // 3

                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True


def empty_board() -> list[list[str]]:
    return [["."] * 9 for _ in range(9)]


if __name__ == "__main__":
    s = Solution()

    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(board1) is True

    board2 = [row[:] for row in board1]
    board2[0][0] = "8"
    assert s.isValidSudoku(board2) is False

    # tablero vacio
    assert s.isValidSudoku(empty_board()) is True

    # repetido en la misma fila, en cajas distintas
    board = empty_board()
    board[4][0] = "7"
    board[4][8] = "7"
    assert s.isValidSudoku(board) is False

    # repetido en la misma columna, en cajas distintas
    board = empty_board()
    board[0][5] = "2"
    board[8][5] = "2"
    assert s.isValidSudoku(board) is False

    print("ok")
