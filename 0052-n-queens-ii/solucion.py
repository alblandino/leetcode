class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diagonals = set()  # row - col
        anti_diagonals = set()  # row + col

        def count_from(row: int) -> int:
            if row == n:
                return 1

            total = 0
            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                total += count_from(row + 1)

                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

            return total

        return count_from(0)


if __name__ == "__main__":
    s = Solution()

    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(1) == 1

    assert s.totalNQueens(2) == 0
    assert s.totalNQueens(3) == 0
    assert s.totalNQueens(8) == 92
    assert s.totalNQueens(9) == 352

    print("ok")
