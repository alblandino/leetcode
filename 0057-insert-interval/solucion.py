class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        start, end = newInterval
        i = 0
        n = len(intervals)

        # intervalos que terminan antes de que empiece el nuevo
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # intervalos que se cruzan con el nuevo: se unen todos en uno
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # los que quedan empiezan despues del nuevo
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2], [3, 10], [12, 16]
    ]

    assert s.insert([], [5, 7]) == [[5, 7]]
    assert s.insert([[3, 5]], [1, 2]) == [[1, 2], [3, 5]]
    assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert s.insert([[1, 5]], [5, 7]) == [[1, 7]]

    print("ok")
