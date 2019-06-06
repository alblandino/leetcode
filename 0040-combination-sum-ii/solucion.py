class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = sorted(candidates)
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                # en un mismo nivel no se repite un valor, asi no salen combinaciones duplicadas
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                backtrack(i + 1, remaining - nums[i])
                path.pop()

        backtrack(0, target)
        return result


def normalize(combinations: list[list[int]]) -> list[list[int]]:
    # el orden no importa, se ordena cada combinacion y la lista completa
    return sorted(sorted(combo) for combo in combinations)


if __name__ == "__main__":
    s = Solution()

    assert normalize(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert normalize(s.combinationSum2([2, 5, 2, 1, 2], 5)) == [[1, 2, 2], [5]]

    # muchas copias del mismo numero
    assert s.combinationSum2([1, 1, 1, 1], 2) == [[1, 1]]
    # no alcanza para llegar a target
    assert s.combinationSum2([3], 2) == []
    # hay que usar todos los numeros
    assert s.combinationSum2([2, 3], 5) == [[2, 3]]

    print("ok")
