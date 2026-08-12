class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=0
        for i in nums:
            c=0
            while i>0:
                c+=1
                i//=10
            if c%2==0:
                t+=1
        return t