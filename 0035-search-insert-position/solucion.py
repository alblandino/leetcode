class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # al salir, left es la primera posicion con un valor mayor que target
        return left


if __name__ == "__main__":
    s = Solution()

    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4

    # va antes de todos
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    # un solo elemento con negativos
    assert s.searchInsert([-5], -5) == 0
    assert s.searchInsert([-5], -10) == 0
    assert s.searchInsert([-5], 3) == 1

    print("ok")
