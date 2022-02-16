class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for numbers in nums:
            while nums.count(numbers) > 1 :
                nums.remove(numbers)
        return len(nums)