class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = sorted(candidates)
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                # estan ordenados: si este se pasa, los siguientes tambien
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                # se pasa i y no i + 1 porque el mismo numero se puede repetir
                backtrack(i, remaining - nums[i])
                path.pop()

        backtrack(0, target)
        return result


def normalize(combinations: list[list[int]]) -> list[list[int]]:
    # el orden no importa, se ordena cada combinacion y la lista completa
    return sorted(sorted(combo) for combo in combinations)


if __name__ == "__main__":
    s = Solution()

    assert normalize(s.combinationSum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    assert normalize(s.combinationSum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSum([2], 1) == []

    # candidatos desordenados
    assert normalize(s.combinationSum([7, 3, 2], 7)) == [[2, 2, 3], [7]]
    # un solo candidato que se repite
    assert s.combinationSum([3], 9) == [[3, 3, 3]]

    print("ok")
