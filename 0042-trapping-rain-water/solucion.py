class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            # se avanza por el lado mas bajo: su agua depende solo de su propio maximo
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water


if __name__ == "__main__":
    s = Solution()

    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9

    # una sola barra
    assert s.trap([5]) == 0
    # escalera: el agua se escurre
    assert s.trap([1, 2, 3, 4]) == 0
    # un hueco entre dos muros iguales
    assert s.trap([3, 0, 3]) == 3

    print("ok")
