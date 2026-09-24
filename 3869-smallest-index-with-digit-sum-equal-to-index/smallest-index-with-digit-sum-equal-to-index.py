class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)):
            val=sum(map(int,str(nums[i])))
            if val==i:
                if ans==-1:
                    ans=val
                else:
                    ans=min(ans,val)
        return ans
