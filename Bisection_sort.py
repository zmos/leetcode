class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len > nums2_len:
            l1 = nums1
            l2 = nums2
        else:
            l1 = nums2
            l2 = nums1
        k = (nums1_len + nums2_len)/2
        f = (nums1_len + nums2_len)%2
        start = 0
        for i in l2:
            if start == k:
                break
            end = len(l1) - 1
            while start <= end:
                if i < l1[(start + end)/2]:
                    end = (start + end)/2 - 1
                else:
                    start = (start + end)/2 + 1
            l1.insert(start, i)
        if f == 0:
            return (l1[k] + l1[k-1])/2.0
        else:
            return l1[k]
