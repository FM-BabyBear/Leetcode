import math as m


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # [0,1,2,4,5,7]
        res = []
        i = 0
        k = 0
        while i < len(nums):
            k = i + 1
            while k < len(nums) and k - i == nums[k] - nums[i]:
                k += 1

            if k - i == 1:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[k - 1]))

            i = k

        return res
