class Solution:
    # Time: O(n) n: length of nums
    # Space: O(1)
    def findClosestNumber(self, nums: list[int]) -> int:
        list = []
        minDiff = 10**9

        for num in nums:
            diff = abs(0 - num)
            if diff < minDiff:
                minDiff = diff
                list.clear()
                list.append(num)
            elif diff == minDiff:
                list.append(num)
        return max(list)

    # Time: O(n) n: length of nums
    # Space: O(1)
    def findClosestNumber2(self, nums: list[int]) -> int:
        close = nums[0]
        midDiff = abs(nums[0])

        for num in nums:
            diff = abs(num)
            if diff < midDiff or (diff == midDiff and num > close):
                midDiff = diff
                close = num

        return close
