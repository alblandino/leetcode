from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # clave: las letras ordenadas, es igual para todas las palabras de un grupo
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


def normalize(groups: list[list[str]]) -> list[list[str]]:
    # el orden no importa, se ordena cada grupo y la lista de grupos
    return sorted(sorted(group) for group in groups)


if __name__ == "__main__":
    s = Solution()

    assert normalize(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == [
        ["ate", "eat", "tea"], ["bat"], ["nat", "tan"]
    ]
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]

    # palabras repetidas van en el mismo grupo
    assert normalize(s.groupAnagrams(["ab", "ba", "ab"])) == [["ab", "ab", "ba"]]
    # ninguna es anagrama de otra
    assert normalize(s.groupAnagrams(["abc", "abd", ""])) == [[""], ["abc"], ["abd"]]

    print("ok")
