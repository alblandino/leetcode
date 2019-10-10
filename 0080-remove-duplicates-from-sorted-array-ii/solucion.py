class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # write es la posicion donde va el siguiente numero que se queda
        write = 0

        for num in nums:
            # si es igual al de dos lugares atras, ya hay dos copias escritas
            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1

        return write


def check(s: Solution, nums: list[int], expected: list[int]) -> bool:
    # revisa el valor devuelto y la parte inicial del arreglo modificado
    k = s.removeDuplicates(nums)
    return k == len(expected) and nums[:k] == expected


if __name__ == "__main__":
    s = Solution()

    assert check(s, [1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3])
    assert check(s, [0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3])
    assert check(s, [1], [1])
    assert check(s, [2, 2, 2, 2], [2, 2])
    assert check(s, [-1, -1, -1, 0, 0, 0, 0, 5], [-1, -1, 0, 0, 5])
    assert check(s, [1, 2, 3], [1, 2, 3])

    print("ok")
