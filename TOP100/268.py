class Solution:
    # Time: O(n) space: O(1)
    def missingNumber(self, nums: list[int]) -> int:
        length = len(nums)

        expectSum = length * (length + 1) // 2
        actualSum = sum(nums)

        return expectSum - actualSum

    # Time: O(nlogn) space: O(1)
    def missingNumber2(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1

        return len(nums) if nums[0] == 0 else 0
