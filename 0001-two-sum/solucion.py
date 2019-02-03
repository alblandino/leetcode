class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # numero -> indice de los que ya se vieron
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([-3, 4, 3, 90], 0) == [0, 2]

    print("ok")
