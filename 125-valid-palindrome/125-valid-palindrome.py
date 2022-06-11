class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        newS=""
        for i in s:
            if ord(i) in range(97, 123): 
                newS += i
            elif ord(i) in range(48, 58):
                newS += i
            else:
                newS = newS
        # if len(newS)<=1:
        #     return True
        # if newS==newS[::-1]:
        #     return True
        # else:
        #     return False
        l=0
        r=len(newS)-1
        while l<r:
            if newS[l] == newS[r]:
                l+=1
                r-=1
            elif newS[l] != newS[r]:
                return False
        return True