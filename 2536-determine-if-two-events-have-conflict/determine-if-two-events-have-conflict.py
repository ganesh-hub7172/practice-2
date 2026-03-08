class Solution:
    def haveConflict(self, event1, event2):
        start1, end1 = event1
        start2, end2 = event2
        
        return max(start1, start2) <= min(end1, end2)