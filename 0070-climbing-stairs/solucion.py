class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # formas de llegar a los dos escalones anteriores
        two_back = 1  # escalon 1
        one_back = 2  # escalon 2

        for _ in range(3, n + 1):
            current = one_back + two_back
            two_back = one_back
            one_back = current

        return one_back


if __name__ == "__main__":
    s = Solution()

    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3

    assert s.climbStairs(1) == 1
    assert s.climbStairs(5) == 8
    assert s.climbStairs(45) == 1836311903

    print("ok")
