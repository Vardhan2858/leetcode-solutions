class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=prices[0]
        pr=0
        for i in prices:
            if i<mn:
                mn=i
            pr=max(pr,i-mn)
        return pr