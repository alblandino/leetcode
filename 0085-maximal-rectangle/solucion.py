class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        cols = len(matrix[0])
        # heights[j] = cuantos '1' seguidos hay hacia arriba en la columna j
        heights = [0] * cols
        best = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            best = max(best, self.largest_in_histogram(heights))

        return best

    def largest_in_histogram(self, heights: list[int]) -> int:
        # misma pila monotona del problema 84
        n = len(heights)
        stack = []
        best = 0

        for i in range(n + 1):
            if i < n:
                current = heights[i]
            else:
                current = 0

            while stack and heights[stack[-1]] >= current:
                height = heights[stack.pop()]
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                best = max(best, height * (i - left))

            stack.append(i)

        return best


if __name__ == "__main__":
    s = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert s.maximalRectangle(matrix) == 6
    assert s.maximalRectangle([["0"]]) == 0
    assert s.maximalRectangle([["1"]]) == 1
    assert s.maximalRectangle([["1", "1"], ["1", "1"]]) == 4
    assert s.maximalRectangle([["0", "0"], ["0", "0"]]) == 0
    assert s.maximalRectangle([["1", "0", "1", "1", "1"]]) == 3
    assert s.maximalRectangle([["1"], ["1"], ["0"], ["1"]]) == 2

    print("ok")
