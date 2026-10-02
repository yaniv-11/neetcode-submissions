class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        h=set()
        count=0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l+=1
            h.add(s[r])
            count=max(r-l+1,count)
            
        return count

        