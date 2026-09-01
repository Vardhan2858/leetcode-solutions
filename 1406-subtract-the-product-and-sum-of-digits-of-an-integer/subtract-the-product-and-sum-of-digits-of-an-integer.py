class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,f=0,1
        while n>0:
            r=n%10
            s+=r
            f*=r
            n//=10
        return f-s