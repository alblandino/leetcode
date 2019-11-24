class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        # una IP usa entre 4 y 12 digitos
        if len(s) < 4 or len(s) > 12:
            return []

        result = []
        parts = []

        def is_valid(part: str) -> bool:
            # sin ceros a la izquierda (salvo el "0" solo) y como maximo 255
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start: int) -> None:
            if len(parts) == 4:
                # solo sirve si se usaron todos los digitos
                if start == len(s):
                    result.append(".".join(parts))
                return

            # cada parte tiene de 1 a 3 digitos
            for length in range(1, 4):
                end = start + length
                if end > len(s):
                    break
                part = s[start:end]
                if is_valid(part):
                    parts.append(part)
                    backtrack(end)
                    parts.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.restoreIpAddresses("25525511135")) == ["255.255.11.135", "255.255.111.35"]
    assert s.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert sorted(s.restoreIpAddresses("101023")) == [
        "1.0.10.23",
        "1.0.102.3",
        "10.1.0.23",
        "10.10.2.3",
        "101.0.2.3",
    ]
    assert s.restoreIpAddresses("1111") == ["1.1.1.1"]
    assert s.restoreIpAddresses("123") == []
    assert s.restoreIpAddresses("1234567890123") == []
    assert sorted(s.restoreIpAddresses("010010")) == ["0.10.0.10", "0.100.1.0"]

    print("ok")
