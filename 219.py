class Solution:

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dict = {}

        for index, num in enumerate(nums):
            if num in dict:
                prevIndex = dict[num]
                if index - prevIndex <= k:
                    return True
                else:
                    dict[num] = index
            else:
                dict[num] = index

        return False

    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        s = set()

        for index, num in enumerate(nums):
            if num in s:
                return True
            else:
                s.add(num)
            if len(s) > k:
                s.remove(nums[index - k])

        return False
