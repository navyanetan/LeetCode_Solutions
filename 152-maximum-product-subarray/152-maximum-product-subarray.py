class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mydict ={}
        # if len(nums)==1:
        #     return nums[0]
        # for index in range(len(nums)-1):
        #     mydict[nums[index]*nums[index+1]]=[index,index+1]
        # Output = max(mydict.keys())
        # print(mydict)
        # return Output
        
        temparray1,temparray2= [0 for _ in range(len(nums))],[0 for _ in range(len(nums))]
        temparray1[0]=temparray2[0]=nums[0]
        for i in range(1,len(nums)):
            temparray1[i] = max(temparray1[i-1]*nums[i],temparray2[i-1]*nums[i],nums[i])
            temparray2[i] = min(temparray1[i-1]*nums[i],temparray2[i-1]*nums[i],nums[i])
        return max(temparray1)