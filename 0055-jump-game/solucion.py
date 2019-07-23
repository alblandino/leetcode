class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_index = len(nums) - 1
        farthest = 0  # indice mas lejano alcanzable hasta ahora

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last_index:
                return True

        return True


if __name__ == "__main__":
    s = Solution()

    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False

    assert s.canJump([0]) is True
    assert s.canJump([0, 1]) is False
    assert s.canJump([2, 0, 0]) is True
    assert s.canJump([1, 0, 1, 0]) is False

    print("ok")
