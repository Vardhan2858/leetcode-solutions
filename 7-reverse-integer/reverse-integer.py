class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        s=0
        x=x*sign
        while x>0:
            r=x%10
            s=s*10+r
            x//=10
        s=s*sign
        if s<=2**31-1 and s>=-2**31:
            return s
        else:
            return 0
        