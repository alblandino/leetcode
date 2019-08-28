class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = digits[:]

        for i in range(len(result) - 1, -1, -1):
            if result[i] < 9:
                result[i] += 1
                return result
            # 9 + 1 = 10: queda 0 y se lleva 1 al digito de la izquierda
            result[i] = 0

        # todos eran 9, por ejemplo 999 -> 1000
        return [1] + result


if __name__ == "__main__":
    s = Solution()

    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([9]) == [1, 0]

    assert s.plusOne([0]) == [1]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plusOne([1, 9, 9]) == [2, 0, 0]

    print("ok")
