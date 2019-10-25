class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        # pila de indices con alturas crecientes
        stack = []
        best = 0

        # en i == n se usa una barra imaginaria de altura 0 para vaciar la pila
        for i in range(n + 1):
            if i < n:
                current = heights[i]
            else:
                current = 0

            while stack and heights[stack[-1]] >= current:
                height = heights[stack.pop()]
                # la barra sacada se extiende desde despues del nuevo tope hasta i - 1
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                width = i - left
                best = max(best, height * width)

            stack.append(i)

        return best


if __name__ == "__main__":
    s = Solution()

    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([0]) == 0
    assert s.largestRectangleArea([5]) == 5
    assert s.largestRectangleArea([2, 2, 2]) == 6
    assert s.largestRectangleArea([1, 2, 3, 4, 5]) == 9
    assert s.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12

    print("ok")
