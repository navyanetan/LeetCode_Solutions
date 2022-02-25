class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_str = ""
        for i in digits:
            num_str += str(i)
        num_str = str(int(num_str) + 1)
        l=[]
        for x in num_str:
            l += x
        return l
            
            
        