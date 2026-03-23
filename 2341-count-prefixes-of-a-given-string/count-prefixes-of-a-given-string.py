class Solution:
    def countPrefixes(self, words, s):
        count = 0
        
        for word in words:
            if s.startswith(word):
                count += 1
        
        return count