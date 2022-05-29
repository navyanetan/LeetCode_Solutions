# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        firstTest = 0
        lastTest = n
        ans = 0
        while firstTest <=lastTest:
            
            midTest = (firstTest + lastTest)//2
            if isBadVersion(midTest):
                ans = midTest
                lastTest = midTest - 1     
            else:
                firstTest = midTest + 1         
        return ans