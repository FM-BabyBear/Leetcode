class Solution:
    # devide and conquer
    def majorityElement(self, nums: list[int], low=0, high=float("inf")) -> int:

        if high == float("inf"):
            high = len(nums) - 1

        length = high - low + 1
        mid = (low + high) // 2

        half = length // 2

        if length == 1:
            return nums[low]

        leftMajority = self.majorityElement(nums, low, mid)
        rightMajority = self.majorityElement(nums, mid + 1, high)

        leftCount = 0
        rightCount = 0

        for i in range(low, high + 1):
            if leftMajority != -1 and nums[i] == leftMajority:
                leftCount = leftCount + 1

            if rightMajority != -1 and nums[i] == rightMajority:
                rightCount = leftCount + 1

        if leftCount > half:
            return leftMajority

        if rightCount > half:
            return rightMajority

        return -1
