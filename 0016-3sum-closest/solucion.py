class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # suma exacta, no se puede estar mas cerca
                    return total

        return closest


if __name__ == "__main__":
    s = Solution()

    assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert s.threeSumClosest([0, 0, 0], 1) == 0
    assert s.threeSumClosest([1, 1, 1, 0], -100) == 2
    assert s.threeSumClosest([1, 1, -1, -1, 3], -1) == -1
    assert s.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2) == -2

    print("ok")
