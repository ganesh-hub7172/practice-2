class Solution:
    def countDistinctIntegers(self, nums):
        s = set(nums)
        
        for x in nums:
            rev = int(str(x)[::-1])
            s.add(rev)
            
        return len(s)