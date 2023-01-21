class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        start = 0
        used = {}

        for end, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                ans = max(ans, end - start + 1)
            used[char] = end

        return ans