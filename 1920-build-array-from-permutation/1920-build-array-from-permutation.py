class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newArray = []
        for i in range(len(nums)):
            newArray.append(nums[nums[i]])
        return newArray