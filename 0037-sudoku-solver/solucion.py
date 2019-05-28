class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box_index(r, c)].add(value)

        def backtrack(pos: int) -> bool:
            if pos == len(empty_cells):
                return True

            r, c = empty_cells[pos]
            box = box_index(r, c)

            for digit in "123456789":
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    continue

                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

                if backtrack(pos + 1):
                    return True

                # no funciono, se deshace la eleccion
                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)

            return False

        backtrack(0)


def box_index(r: int, c: int) -> int:
    # numero de caja 3x3, de 0 a 8 leyendo por filas
    return (r // 3) * 3 + c // 3


def is_solved(board: list[list[str]]) -> bool:
    # cada fila, columna y caja debe tener exactamente los digitos del 1 al 9
    digits = set("123456789")
    for i in range(9):
        row = set(board[i])
        col = set(board[r][i] for r in range(9))

        # esquina superior izquierda de la caja i
        top = (i // 3) * 3
        left = (i % 3) * 3
        box = set()
        for r in range(top, top + 3):
            for c in range(left, left + 3):
                box.add(board[r][c])

        if row != digits or col != digits or box != digits:
            return False
    return True


if __name__ == "__main__":
    s = Solution()

    board = [
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
    expected = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    s.solveSudoku(board)
    assert board == expected
    assert is_solved(board)

    # tablero resuelto con una sola casilla vacia
    board = [row[:] for row in expected]
    board[4][4] = "."
    s.solveSudoku(board)
    assert board == expected

    # un tablero ya resuelto no cambia
    board = [row[:] for row in expected]
    s.solveSudoku(board)
    assert board == expected

    print("ok")
