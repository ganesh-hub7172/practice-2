from collections import deque

class Solution:
    def minimumOperations(self, root):
        queue = deque([root])
        total_swaps = 0
        
        while queue:
            size = len(queue)
            level = []
            
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            total_swaps += self.minSwaps(level)
        
        return total_swaps
    
    def minSwaps(self, arr):
        n = len(arr)
        arrpos = list(enumerate(arr))
        
        # sort by value
        arrpos.sort(key=lambda x: x[1])
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or arrpos[i][0] == i:
                continue
            
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][0]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
        
        return swaps