class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z_count=0
        prod=1
        res=[0]*len(nums)
        for i in nums:
            if i==0:
                z_count+=1
                if z_count>1:
                    return res
            else:
                prod*=i
        for i in range(len(nums)):
            if z_count==1:
                if nums[i]==0:
                    res[i]=prod
            else:
                res[i]=prod//nums[i]
        return res