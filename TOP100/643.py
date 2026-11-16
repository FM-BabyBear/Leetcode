class Solution:
    # Time: O(n)
    # Space: O(1)

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        maxSum = sum

        for i in range(k, len(nums)):
            sum = sum + nums[i] - nums[i - k]
            maxSum = max(sum, maxSum)

        return maxSum / k
