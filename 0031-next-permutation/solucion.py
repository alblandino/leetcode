class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. desde la derecha, el primer numero menor que su vecino derecho
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2. desde la derecha, el primer numero mayor que nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3. la parte derecha esta en orden descendente; al invertirla queda la menor posible
        self.reverse_range(nums, i + 1, n - 1)

    def reverse_range(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3]
    s.nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [3, 2, 1]
    s.nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    s.nextPermutation(nums)
    assert nums == [1, 5, 1]

    # un solo elemento
    nums = [4]
    s.nextPermutation(nums)
    assert nums == [4]

    # el cambio no esta al final
    nums = [2, 3, 1]
    s.nextPermutation(nums)
    assert nums == [3, 1, 2]

    # con repetidos
    nums = [1, 5, 1]
    s.nextPermutation(nums)
    assert nums == [5, 1, 1]

    print("ok")
