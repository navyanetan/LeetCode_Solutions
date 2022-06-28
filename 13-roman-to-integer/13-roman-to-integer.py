class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydic={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        output= 0
        previousnumber= 0
        for i in range(len(s)):
            currentnumber = mydic[s[i]]
            output += currentnumber
            if previousnumber<currentnumber:
                output -= previousnumber*2
            previousnumber = currentnumber
        return output