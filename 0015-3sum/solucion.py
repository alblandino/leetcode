class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            # el menor ya es positivo: no hay forma de llegar a 0
            if nums[i] > 0:
                break
            # mismo primer numero que antes: daria tripletas repetidas
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # saltar valores repetidos para no duplicar la tripleta
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert sorted(s.threeSum([-2, 0, 1, 1, 2])) == [[-2, 0, 2], [-2, 1, 1]]
    assert s.threeSum([1, 2, 3]) == []

    print("ok")
