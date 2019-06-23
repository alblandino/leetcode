class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0  # ultimo indice alcanzable con los saltos actuales
        farthest = 0     # lo mas lejos que se llega con un salto mas

        # no se revisa el ultimo indice: al llegar ahi ya no se salta
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


if __name__ == "__main__":
    s = Solution()

    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2

    # ya se esta en el final
    assert s.jump([0]) == 0
    # un salto basta aunque sobre alcance
    assert s.jump([5, 1, 1]) == 1
    # solo se puede avanzar de uno en uno
    assert s.jump([1, 1, 1, 1]) == 3

    print("ok")
