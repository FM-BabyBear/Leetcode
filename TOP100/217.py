class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        map = set()

        for n in nums:
            if n in map:
                return True
            else:
                map.add(n)

        return False

    def containsDuplicate2(self, nums: list[int]) -> bool:
        sortedNums = sorted(nums)

        for i in range(len(nums) - 1):
            if sortedNums[i] == sortedNums[i + 1]:
                return True

        return False
