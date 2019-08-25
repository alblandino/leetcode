class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exponent = False

        for i, char in enumerate(s):
            if "0" <= char <= "9":
                seen_digit = True
            elif char in "+-":
                # el signo solo va al inicio o justo despues de la e
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char == ".":
                # un solo punto y nunca dentro del exponente
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                # una sola e y con digitos antes
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # el exponente necesita sus propios digitos
            else:
                return False

        return seen_digit


if __name__ == "__main__":
    s = Solution()

    assert s.isNumber("0") is True
    assert s.isNumber("e") is False
    assert s.isNumber(".") is False

    # lista de validos del enunciado
    valid = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
             "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for text in valid:
        assert s.isNumber(text) is True, text

    # lista de invalidos del enunciado
    invalid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for text in invalid:
        assert s.isNumber(text) is False, text

    # casos borde propios
    extra_valid = ["1.e5", "+.8", "46.e3", "-1E-16", "005047e+6"]
    for text in extra_valid:
        assert s.isNumber(text) is True, text

    extra_invalid = ["+", "-.", ".e1", "1e+", "1+", "6e6.5", ".1.", "+e",
                     "1ee5", "inf", "Infinity", "nan", "e9", "4e+-5", "..", "1e5e"]
    for text in extra_invalid:
        assert s.isNumber(text) is False, text

    print("ok")
