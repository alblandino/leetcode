class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        current = []

        def backtrack(start: int) -> None:
            if len(current) == k:
                result.append(current[:])
                return

            # poda: el ultimo numero que se puede elegir aqui deja espacio para completar k
            remaining = k - len(current)
            last = n - remaining + 1
            for num in range(start, last + 1):
                current.append(num)
                backtrack(num + 1)
                current.pop()

        backtrack(1)
        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combine(1, 1) == [[1]]
    assert s.combine(3, 3) == [[1, 2, 3]]
    assert sorted(s.combine(4, 1)) == [[1], [2], [3], [4]]
    assert len(s.combine(10, 3)) == 120

    print("ok")
