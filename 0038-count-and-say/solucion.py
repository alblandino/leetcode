class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = self.run_length_encode(result)
        return result

    def run_length_encode(self, digits: str) -> str:
        # cada grupo de digitos iguales se escribe como "cantidad + digito"
        parts = []
        i = 0

        while i < len(digits):
            j = i
            while j < len(digits) and digits[j] == digits[i]:
                j += 1
            parts.append(str(j - i) + digits[i])
            i = j

        return "".join(parts)


if __name__ == "__main__":
    s = Solution()

    assert s.countAndSay(4) == "1211"
    assert s.countAndSay(1) == "1"

    # siguientes terminos conocidos de la secuencia
    assert s.countAndSay(2) == "11"
    assert s.countAndSay(5) == "111221"
    assert s.countAndSay(6) == "312211"
    # el limite superior corre sin problema
    assert s.countAndSay(30).startswith("3113")

    print("ok")
