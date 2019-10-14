class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                # con los tres iguales no se sabe que mitad esta ordenada
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                # la mitad izquierda esta ordenada
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # la mitad derecha esta ordenada
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":
    s = Solution()

    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert s.search([1], 1) is True
    assert s.search([1], 0) is False
    assert s.search([1, 0, 1, 1, 1], 0) is True
    assert s.search([1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1], 13) is True
    assert s.search([3, 1], 1) is True

    print("ok")
