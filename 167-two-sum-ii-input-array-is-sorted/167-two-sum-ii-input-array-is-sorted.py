class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for index,value in enumerate(numbers):
            checkingValue = target - numbers[index]
            if checkingValue in dictionary:
                return [dictionary[checkingValue]+1,index+1] 
            dictionary[value] = index