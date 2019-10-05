class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]

        for num in nums:
            # cada subconjunto que ya existe genera otro con num agregado
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])
            result.extend(new_subsets)

        return result


def normalize(subsets: list[list[int]]) -> list[list[int]]:
    # ordena cada subconjunto y la lista completa para comparar sin importar el orden
    return sorted(sorted(subset) for subset in subsets)


if __name__ == "__main__":
    s = Solution()

    assert normalize(s.subsets([1, 2, 3])) == normalize(
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert normalize(s.subsets([0])) == normalize([[], [0]])
    assert normalize(s.subsets([-1, 5])) == normalize([[], [-1], [5], [-1, 5]])
    assert len(s.subsets(list(range(10)))) == 1024

    print("ok")
