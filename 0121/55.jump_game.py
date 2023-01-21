class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos = nums[0]
        for i, num in enumerate(nums):
            if i > pos:
                return False
            pos = max(pos, i + num)
            if pos >= len(nums) - 1:
                return True
        return True