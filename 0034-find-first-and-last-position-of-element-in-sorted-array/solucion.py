class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.find_edge(nums, target, True)
        if first == -1:
            return [-1, -1]

        last = self.find_edge(nums, target, False)
        return [first, last]

    def find_edge(self, nums: list[int], target: int, leftmost: bool) -> int:
        left, right = 0, len(nums) - 1
        found = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # se guarda y se sigue buscando hacia el borde pedido
                found = mid
                if leftmost:
                    right = mid - 1
                else:
                    left = mid + 1

        return found


if __name__ == "__main__":
    s = Solution()

    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert s.searchRange([], 0) == [-1, -1]

    # un solo elemento
    assert s.searchRange([1], 1) == [0, 0]
    # todo el arreglo es target
    assert s.searchRange([2, 2, 2, 2], 2) == [0, 3]
    # target en los extremos
    assert s.searchRange([-3, -3, 0, 9], -3) == [0, 1]
    assert s.searchRange([-3, 0, 9, 9], 9) == [2, 3]

    print("ok")
