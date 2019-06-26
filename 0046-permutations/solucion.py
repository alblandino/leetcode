class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
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
    assert sorted(s.permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(s.permute([0, 1])) == [[0, 1], [1, 0]]
    assert s.permute([1]) == [[1]]

    # negativos
    assert sorted(s.permute([-1, 5])) == [[-1, 5], [5, -1]]
    # tamano maximo: 6! permutaciones, todas distintas
    result = s.permute([1, 2, 3, 4, 5, 6])
    assert len(result) == 720
    assert len(set(tuple(p) for p in result)) == 720

    print("ok")
