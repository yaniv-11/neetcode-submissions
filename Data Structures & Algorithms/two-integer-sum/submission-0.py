class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res in hash:
                return [hash[res],i]
            hash[nums[i]]=i
        return []