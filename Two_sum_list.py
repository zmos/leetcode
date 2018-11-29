class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = nums
        target = target
        p = 0
        while l:
            j = target - l[0]
            l.pop(0)
            p = p + 1
            if j in l:
                return [p-1, l.index(j)+p]
