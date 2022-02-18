class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = len(nums)
        # nums2 = nums.copy()
        # for no in range(len(nums)):
        #     i = nums.index(val)
        #     if no == i:
        #         k -= 1
        #         nums.pop(i)
        #         nums.append(nums2[i])
        # return k 
        k = len(nums)
        counter = nums.count(val)
        while counter:
            nums.remove(val)
            counter -=1
            k -=1
        return k 
        