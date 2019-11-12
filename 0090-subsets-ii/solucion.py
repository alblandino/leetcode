class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # ordenar deja juntos los valores iguales
        nums = sorted(nums)
        result = []
        current = []

        def backtrack(start: int) -> None:
            result.append(current[:])
            for i in range(start, len(nums)):
                # en el mismo nivel, un valor repetido daria los mismos subconjuntos
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result


def normalize(subsets: list[list[int]]) -> list[list[int]]:
    # ordena cada subconjunto y la lista completa para comparar sin importar el orden
    return sorted(sorted(subset) for subset in subsets)


if __name__ == "__main__":
    s = Solution()

    assert normalize(s.subsetsWithDup([1, 2, 2])) == normalize(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )
    assert normalize(s.subsetsWithDup([0])) == normalize([[], [0]])
    assert normalize(s.subsetsWithDup([2, 2, 2])) == normalize([[], [2], [2, 2], [2, 2, 2]])
    assert normalize(s.subsetsWithDup([4, 4, 1, 4])) == normalize(
        [[], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4]]
    )
    assert normalize(s.subsetsWithDup([3, -1])) == normalize([[], [-1], [3], [-1, 3]])

    print("ok")
