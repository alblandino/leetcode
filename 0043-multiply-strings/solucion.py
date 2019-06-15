class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # el producto tiene como maximo len(num1) + len(num2) digitos
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")
            for j in range(len(num2) - 1, -1, -1):
                digit2 = ord(num2[j]) - ord("0")
                # num1[i] * num2[j] cae en las posiciones i + j (acarreo) e i + j + 1
                total = digit1 * digit2 + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        # quitar ceros a la izquierda
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return "".join(str(digit) for digit in result[start:])


if __name__ == "__main__":
    s = Solution()

    assert s.multiply("2", "3") == "6"
    assert s.multiply("123", "456") == "56088"

    # multiplicar por cero
    assert s.multiply("0", "52") == "0"
    assert s.multiply("9133", "0") == "0"
    # muchos acarreos
    assert s.multiply("999", "999") == "998001"
    # un solo digito por un numero largo
    assert s.multiply("1", "123456789") == "123456789"

    print("ok")
