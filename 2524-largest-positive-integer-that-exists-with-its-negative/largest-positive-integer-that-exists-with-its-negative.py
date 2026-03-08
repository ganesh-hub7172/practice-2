class Solution:
    def findMaxK(self, nums):
        s = set(nums)
        ans = -1
        
        for num in nums:
            if num > 0 and -num in s:
                ans = max(ans, num)
                
        return ans