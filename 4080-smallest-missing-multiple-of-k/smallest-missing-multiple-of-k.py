class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=1
        for i in range(len(nums)):
            if k*n in nums:
                n+=1
            else:
                return k*n
        return k*n

        