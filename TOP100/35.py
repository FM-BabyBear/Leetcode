class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = len(nums)

        left = 0
        right = l - 1
        mid = (left + right) // 2

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return mid + 1
