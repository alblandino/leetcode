from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = len(words)
        if word_len * word_count > len(s):
            return []

        need = Counter(words)
        result = []

        # una pasada por cada desplazamiento posible dentro de una palabra
        for offset in range(word_len):
            left = offset
            window = Counter()
            used = 0  # palabras dentro de la ventana

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in need:
                    # ninguna respuesta puede incluir esta palabra, se empieza despues de ella
                    window.clear()
                    used = 0
                    left = right + word_len
                    continue

                window[word] += 1
                used += 1

                # si sobra una copia de la palabra, se achica la ventana por la izquierda
                while window[word] > need[word]:
                    first = s[left:left + word_len]
                    window[first] -= 1
                    used -= 1
                    left += word_len

                if used == word_count:
                    result.append(left)
                    # se saca la primera palabra para seguir buscando
                    first = s[left:left + word_len]
                    window[first] -= 1
                    used -= 1
                    left += word_len

        return result


if __name__ == "__main__":
    s = Solution()

    # la respuesta puede venir en cualquier orden
    assert sorted(s.findSubstring("barfoothefoobarman", ["foo", "bar"])) == [0, 9]
    assert s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
    assert sorted(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])) == [6, 9, 12]

    # las palabras juntas son mas largas que s
    assert s.findSubstring("a", ["aa"]) == []
    # palabras repetidas y respuestas que se traslapan
    assert sorted(s.findSubstring("aaaaaa", ["aa", "aa"])) == [0, 1, 2]
    # una palabra que aparece mas veces de las permitidas
    assert s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]

    print("ok")
