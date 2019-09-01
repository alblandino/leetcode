class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        # los digitos se armaron del menos al mas significativo
        result.reverse()
        return "".join(result)


if __name__ == "__main__":
    s = Solution()

    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"

    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("1", "1") == "10"
    assert s.addBinary("1111", "1") == "10000"
    assert s.addBinary("0", "101") == "101"

    print("ok")
