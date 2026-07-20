class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        arr=[]
        for i,j in d.items():
            arr.append([j,i])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res