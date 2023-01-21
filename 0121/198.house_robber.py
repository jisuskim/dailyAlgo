class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        for i in nums:
            start, end = end, max(start+i,end)
        return end