class Solution:
    # Time: O(logn) n: length of nums
    # Space: O(1)
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1

    # Time: O(logn) n: length of nums
    # Space: O(1)
    def search2(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1

    # Time: O(logn) n: length of nums
    # Space: O(1)
    def search3(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1
