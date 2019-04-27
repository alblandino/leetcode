class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # k es la posicion donde va el siguiente elemento que se queda
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    s = Solution()

    # el orden de los primeros k no importa, por eso se compara ordenando
    nums = [3, 2, 2, 3]
    k = s.removeElement(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums, 2)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

    # arreglo vacio
    nums = []
    k = s.removeElement(nums, 0)
    assert k == 0

    # todos son val
    nums = [4, 4, 4]
    k = s.removeElement(nums, 4)
    assert k == 0

    # val no aparece
    nums = [1, 2, 3]
    k = s.removeElement(nums, 50)
    assert k == 3
    assert nums == [1, 2, 3]

    print("ok")
