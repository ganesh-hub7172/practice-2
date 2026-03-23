class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        maxProd = [[0] * n for _ in range(m)]
        minProd = [[0] * n for _ in range(m)]
        
        maxProd[0][0] = grid[0][0]
        minProd[0][0] = grid[0][0]
        
        # First column
        for i in range(1, m):
            maxProd[i][0] = maxProd[i-1][0] * grid[i][0]
            minProd[i][0] = maxProd[i][0]
        
        # First row
        for j in range(1, n):
            maxProd[0][j] = maxProd[0][j-1] * grid[0][j]
            minProd[0][j] = maxProd[0][j]
        
        # Fill rest
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                candidates = [
                    val * maxProd[i-1][j],
                    val * minProd[i-1][j],
                    val * maxProd[i][j-1],
                    val * minProd[i][j-1]
                ]
                
                maxProd[i][j] = max(candidates)
                minProd[i][j] = min(candidates)
        
        result = maxProd[m-1][n-1]
        
        if result < 0:
            return -1
        return result % MOD