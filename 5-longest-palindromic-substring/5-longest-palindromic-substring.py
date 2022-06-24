class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        resultlen= len(result)
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resultlen: 
                    resultlen= r-l+1
                    result=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resultlen: 
                    resultlen= r-l+1
                    result=s[l:r+1]
                l-=1
                r+=1
        return result