class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # ultimo elemento real de nums1
        j = n - 1  # ultimo elemento de nums2
        write = m + n - 1  # posicion donde va el siguiente mayor

        # se llena desde atras para no pisar valores de nums1 sin usar
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1


if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    assert s.merge(nums1, 3, [2, 5, 6], 3) is None
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    s.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [4, 5, 6, 0, 0, 0]
    s.merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    nums1 = [-5, 3, 0, 0]
    s.merge(nums1, 2, [-7, 10], 2)
    assert nums1 == [-7, -5, 3, 10]

    print("ok")
