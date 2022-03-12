class Solution(object):
    def binarysearch(self,arr,target):
        if len(arr) == 1 and arr[0]!=target:
            return False
        center_index = len(arr)//2
        if target ==arr[center_index]:
            return True
        if target < arr[center_index]:
            return self.binarysearch(arr[:center_index],target)
        elif target> arr[center_index]:
            return self.binarysearch(arr[center_index:],target) 
        
    def searchMatrix(self, matrix, target):        
        if len(matrix)==0:
            return False
        i = len(matrix)//2
        row = matrix[i]
        if target == row[0]:
            return True
        if target == row[-1]:
            return True
        elif target > row[-1]:
            return self.searchMatrix(matrix[i+1:], target)              
        elif target < row[0]:
            return self.searchMatrix(matrix[:i], target)
        else:
            return self.binarysearch(row, target)
     

        
    