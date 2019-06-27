class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                # de un valor repetido solo se toma una copia si la anterior ya esta en el camino
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == "__main__":
    s = Solution()

    # la respuesta puede venir en cualquier orden
    assert sorted(s.permuteUnique([1, 1, 2])) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert sorted(s.permuteUnique([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # todos iguales
    assert s.permuteUnique([2, 2, 2]) == [[2, 2, 2]]
    # un solo elemento
    assert s.permuteUnique([-10]) == [[-10]]
    # dos parejas de repetidos: 4! / (2! * 2!) = 6
    assert sorted(s.permuteUnique([2, 1, 2, 1])) == [
        [1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]
    ]

    print("ok")
