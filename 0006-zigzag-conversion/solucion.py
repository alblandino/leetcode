class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        step = 1  # 1 baja, -1 sube

        for char in s:
            rows[row] += char
            # en los bordes se cambia de direccion
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return "".join(rows)


if __name__ == "__main__":
    s = Solution()

    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert s.convert("A", 1) == "A"
    assert s.convert("AB", 1) == "AB"
    assert s.convert("ABCD", 2) == "ACBD"
    assert s.convert("AB", 5) == "AB"

    print("ok")
