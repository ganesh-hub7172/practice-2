class Solution:
    def kWeakestRows(self, mat, k):
        arr = []
        
        for i in range(len(mat)):
            soldiers = sum(mat[i])
            arr.append((soldiers, i))
        
        arr.sort()
        
        result = []
        for i in range(k):
            result.append(arr[i][1])
        
        return result