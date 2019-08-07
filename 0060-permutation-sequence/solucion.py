class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # factorials[i] = i!
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i

        available = [str(digit) for digit in range(1, n + 1)]
        k -= 1  # contar desde 0 facilita las divisiones
        result = []

        for remaining in range(n, 0, -1):
            # cada numero inicial abarca un bloque de (remaining - 1)! permutaciones
            block_size = factorials[remaining - 1]
            index = k // block_size
            k = k % block_size
            result.append(available.pop(index))

        return "".join(result)


if __name__ == "__main__":
    s = Solution()

    assert s.getPermutation(3, 3) == "213"
    assert s.getPermutation(4, 9) == "2314"
    assert s.getPermutation(3, 1) == "123"

    assert s.getPermutation(1, 1) == "1"
    assert s.getPermutation(3, 6) == "321"
    assert s.getPermutation(4, 24) == "4321"
    assert s.getPermutation(9, 1) == "123456789"
    assert s.getPermutation(9, 362880) == "987654321"

    print("ok")
