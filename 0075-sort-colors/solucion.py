class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # modifica nums en el lugar, no devuelve nada
        low = 0  # siguiente posicion para un 0
        mid = 0  # elemento que se esta revisando
        high = len(nums) - 1  # siguiente posicion para un 2

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                # no se avanza mid: el valor que llego de high aun no se reviso
                high -= 1


if __name__ == "__main__":
    s = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    assert s.sortColors(nums) is None
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    s.sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [0]
    s.sortColors(nums)
    assert nums == [0]

    nums = [2, 2, 0]
    s.sortColors(nums)
    assert nums == [0, 2, 2]

    nums = [1, 0]
    s.sortColors(nums)
    assert nums == [0, 1]

    nums = [2, 1, 0, 2, 1, 0, 1]
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 1, 2, 2]

    print("ok")
