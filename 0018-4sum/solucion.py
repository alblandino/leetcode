class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []

        for a in range(n - 3):
            # mismo primer numero que antes: daria grupos repetidos
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                left, right = b + 1, n - 1
                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[a], nums[b], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.fourSum([1, 0, -1, 0, -2, 2], 0)) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert s.fourSum([1, 2, 3], 6) == []
    assert s.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
    assert s.fourSum([1000000000, 1000000000, 1000000000, 1000000000], -294967296) == []

    print("ok")
