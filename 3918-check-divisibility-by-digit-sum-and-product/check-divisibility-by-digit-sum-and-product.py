class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        r=1
        l=n
        while n>0:
            k=n%10
            s+=k
            r=r*k
            n//=10
        return l%(s+r)==0
        