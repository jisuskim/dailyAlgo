class Solution(object):
    def wordBreak(self, s, wordDict):
        length = len(s)
        word_set = set(wordDict)
        dp = [False] * (length + 1)
        dp[length] = True

        for i in range(length, -1, -1):
            for j in range(i):
                if dp[i] and s[j:i] in word_set:
                    dp[j] = True
        return dp[0]