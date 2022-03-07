# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:        
        start = 0
        end = n
        ans = n
        while start<=end:
            mid = (start+end) // 2
            if isBadVersion(mid) == False:
                start = mid+1
            elif isBadVersion(mid) == True:
                end = mid-1
                ans = mid
        return ans
