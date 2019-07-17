class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        current = nums[0]  # mejor suma de un tramo que termina en i

        for i in range(1, len(nums)):
            # si lo acumulado es negativo conviene empezar de nuevo en nums[i]
            current = max(nums[i], current + nums[i])
            best = max(best, current)

        return best


if __name__ == "__main__":
    s = Solution()

    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23

    assert s.maxSubArray([-1]) == -1
    assert s.maxSubArray([-3, -2, -5]) == -2
    assert s.maxSubArray([2, -10, 3]) == 3

    print("ok")
