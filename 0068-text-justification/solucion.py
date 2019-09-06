def left_justify(line_words: list[str], max_width: int) -> str:
    line = " ".join(line_words)
    return line + " " * (max_width - len(line))


def full_justify(line_words: list[str], letters: int, max_width: int) -> str:
    gaps = len(line_words) - 1
    total_spaces = max_width - letters
    base_spaces = total_spaces // gaps
    extra_spaces = total_spaces % gaps  # los primeros huecos llevan uno mas

    parts = []
    for i in range(gaps):
        spaces = base_spaces
        if i < extra_spaces:
            spaces += 1
        parts.append(line_words[i] + " " * spaces)
    parts.append(line_words[-1])

    return "".join(parts)


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        i = 0

        while i < len(words):
            # meter tantas palabras como quepan con un espacio entre cada una
            j = i
            letters = 0
            while j < len(words) and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            line_words = words[i:j]
            is_last_line = j == len(words)

            if is_last_line or len(line_words) == 1:
                lines.append(left_justify(line_words, maxWidth))
            else:
                lines.append(full_justify(line_words, letters, maxWidth))

            i = j

        return lines


if __name__ == "__main__":
    s = Solution()

    assert s.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    ) == [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ]
    assert s.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16
    ) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ]
    assert s.fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
         "we", "do"],
        20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]

    assert s.fullJustify(["a"], 1) == ["a"]
    assert s.fullJustify(["a", "b", "c", "d"], 1) == ["a", "b", "c", "d"]
    assert s.fullJustify(["a", "b", "c"], 3) == ["a b", "c  "]
    assert s.fullJustify(
        ["Listen", "to", "many,", "speak", "to", "a", "few."], 6
    ) == ["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "]

    # toda linea debe medir exactamente maxWidth
    for line in s.fullJustify(["one", "two", "three", "four", "five", "six"], 11):
        assert len(line) == 11

    print("ok")
