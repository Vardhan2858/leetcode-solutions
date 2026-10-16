class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s=[]
        i,j=0,0
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                s.append(nums1[i])
                i+=1
    
            else:
                s.append(nums2[j])
                j+=1
        s.extend(nums1[i:])
        s.extend(nums2[j:])
        l=len(s)
        if l%2==0:
            return (s[l//2]+s[(l/2)-1])/2.0
        else:
            return s[l//2]

        
