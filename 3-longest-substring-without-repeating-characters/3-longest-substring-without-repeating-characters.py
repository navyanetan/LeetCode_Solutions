class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # mydictionary = {}
        # for index,value in enumerate(s):
        #     if s[index]!=s[index+1]:
        #         mydictionary[value]=index
        #     else:
        #         return len(mydictionary)
        characterset= set()
        l = 0
        output=0
        for r in range(len(s)):
            while s[r] in characterset:
                characterset.remove(s[l])
                l=l+1
            characterset.add(s[r])
            output = max(output,r-l+1)
        return output