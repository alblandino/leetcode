class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # al menos una de las dos mitades esta ordenada
            if nums[left] <= nums[mid]:
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

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1

    # un elemento que si esta
    assert s.search([1], 1) == 0
    # sin rotacion
    assert s.search([1, 2, 3, 4, 5], 4) == 3
    # rotado con dos elementos y con el valor en el borde izquierdo
    assert s.search([3, 1], 1) == 1
    assert s.search([5, 1, 3], 5) == 0

    print("ok")
