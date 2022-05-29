class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beginIndex = 0
        length = len(nums)-1
        while beginIndex<=length:
            midTermIndex = (beginIndex + length)//2
            midTerm = nums[midTermIndex]
            if target == midTerm:
                return midTermIndex
            elif target<midTerm:
                length = midTermIndex-1
            elif target>midTerm:
                beginIndex = midTermIndex+1
        return -1
        
        