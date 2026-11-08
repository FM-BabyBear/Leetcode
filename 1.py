# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=arw5ns9e

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        length = len(nums)

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment], i]
            else:
                hashmap[nums[i]] = i

        return []
