class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)
        if j <=1:
            return nums
        while i < j: 
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                i -= 1
                j -= 1    
            i = i + 1    
                