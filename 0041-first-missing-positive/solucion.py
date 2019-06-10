class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # cada valor v entre 1 y n se manda a la posicion v - 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # la primera posicion que no tiene su valor indica el que falta
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":
    s = Solution()

    assert s.firstMissingPositive([1, 2, 0]) == 3
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1

    # un solo elemento
    assert s.firstMissingPositive([1]) == 2
    assert s.firstMissingPositive([-2147483648]) == 1
    # repetidos
    assert s.firstMissingPositive([1, 1, 2, 2]) == 3
    # ya estan todos de 1 a n, desordenados
    assert s.firstMissingPositive([2, 1]) == 3

    print("ok")
