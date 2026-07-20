class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        mid=len(l)//2
        return l==l[::-1]
