class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                # mid sirve; se busca uno mayor que tambien sirva
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer


if __name__ == "__main__":
    s = Solution()

    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2

    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    assert s.mySqrt(15) == 3
    assert s.mySqrt(16) == 4
    assert s.mySqrt(2147483647) == 46340

    print("ok")
