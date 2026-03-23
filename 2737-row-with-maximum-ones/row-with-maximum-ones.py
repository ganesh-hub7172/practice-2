class Solution:
    def rowAndMaximumOnes(self, mat):
        maxCount = 0
        index = 0
        
        for i in range(len(mat)):
            count = sum(mat[i])
            
            if count > maxCount:
                maxCount = count
                index = i
        
        return [index, maxCount]