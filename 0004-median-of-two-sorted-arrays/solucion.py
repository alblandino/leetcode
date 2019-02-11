class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # la busqueda binaria se hace sobre el arreglo mas corto
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            # cut1 elementos de nums1 y cut2 de nums2 forman la mitad izquierda
            cut1 = (low + high) // 2
            cut2 = half - cut1

            left1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            right1 = nums1[cut1] if cut1 < m else float("inf")
            left2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
            right2 = nums2[cut2] if cut2 < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                # se tomaron demasiados de nums1
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0


if __name__ == "__main__":
    s = Solution()

    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([2], []) == 2.0
    assert s.findMedianSortedArrays([1, 2], [-1, 3]) == 1.5
    assert s.findMedianSortedArrays([5, 6, 7], [1, 2, 3, 4]) == 4.0

    print("ok")
