class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beginIndex = 0
        lastIndex = len(nums)- 1
        if target<nums[0]:
            return 0
        if target>nums[lastIndex]:
            return lastIndex + 1
        while beginIndex <= lastIndex:
            centerIndex = (beginIndex + lastIndex)//2
            center = nums[centerIndex]
            if beginIndex==lastIndex:
                return beginIndex
            if center==target:
                return centerIndex
            elif center>target:
                lastIndex= centerIndex
            elif center<target:
                beginIndex = centerIndex+1
        