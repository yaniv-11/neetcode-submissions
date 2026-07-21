class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] and i>0:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                threesome=nums[i]+nums[j]+nums[k]
                if threesome==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif threesome>0:
                    k-=1
                else:
                    j+=1
        return res      
        