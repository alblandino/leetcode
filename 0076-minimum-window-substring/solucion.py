class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # cuantas veces le falta cada letra de t a la ventana
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        missing = len(t)  # letras de t que aun no estan cubiertas
        left = 0
        best_start = 0
        best_len = len(s) + 1

        for right, ch in enumerate(s):
            if ch in need:
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1

            # la ventana ya cubre todo t: se intenta achicar por la izquierda
            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_start = left
                    best_len = window_len

                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    # si esa letra vuelve a faltar, la ventana deja de ser valida
                    if need[left_ch] > 0:
                        missing += 1
                left += 1

        if best_len > len(s):
            return ""
        return s[best_start:best_start + best_len]


if __name__ == "__main__":
    s = Solution()

    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    assert s.minWindow("ab", "b") == "b"
    assert s.minWindow("bba", "ab") == "ba"
    assert s.minWindow("aAbB", "AB") == "AbB"
    assert s.minWindow("abc", "d") == ""

    print("ok")
