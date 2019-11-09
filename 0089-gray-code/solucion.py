class Solution:
    def grayCode(self, n: int) -> list[int]:
        # codigo de 0 bits: solo el 0
        result = [0]

        for bit in range(n):
            # copia en espejo con el bit nuevo prendido
            new_bit_value = 2 ** bit
            mirrored = []
            for value in reversed(result):
                mirrored.append(value + new_bit_value)
            result = result + mirrored

        return result


def differ_by_one_bit(a: int, b: int, n: int) -> bool:
    # compara las representaciones binarias de largo n caracter por caracter
    bits_a = format(a, "b").zfill(n)
    bits_b = format(b, "b").zfill(n)
    differences = 0
    for x, y in zip(bits_a, bits_b):
        if x != y:
            differences += 1
    return differences == 1


def is_valid_gray_code(sequence: list[int], n: int) -> bool:
    size = 2 ** n
    if len(sequence) != size or sequence[0] != 0:
        return False
    if sorted(sequence) != list(range(size)):
        return False
    for i in range(size):
        # el siguiente del ultimo es el primero
        next_value = sequence[(i + 1) % size]
        if not differ_by_one_bit(sequence[i], next_value, n):
            return False
    return True


if __name__ == "__main__":
    s = Solution()

    assert s.grayCode(2) == [0, 1, 3, 2]
    assert s.grayCode(1) == [0, 1]
    assert s.grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4]
    for n in range(1, 17):
        assert is_valid_gray_code(s.grayCode(n), n)

    print("ok")
