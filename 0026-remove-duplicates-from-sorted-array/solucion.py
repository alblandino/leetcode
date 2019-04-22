class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # k es la posicion donde va el siguiente valor unico
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]

    # un solo elemento
    nums = [7]
    k = s.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [7]

    # todos iguales y negativos
    nums = [-3, -3, -3]
    k = s.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [-3]

    # sin repetidos, el arreglo queda igual
    nums = [-100, 0, 100]
    k = s.removeDuplicates(nums)
    assert k == 3
    assert nums == [-100, 0, 100]

    print("ok")
