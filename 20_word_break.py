class Solution(object):
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for char in range(len(s) -1, -1, -1):
            for word in wordDict:
                if (char + len(word)) <= len(s) and s[char : char + len(word)] == word:
                    dp[char] = dp[char + len(word)]
                if dp[char]:
                    break
        return dp[0]
    
a = Solution()
print(a.wordBreak("leetcode",["leet","code"]))
print(a.wordBreak("applepenapple",["apple","pen"]))
print(a.wordBreak("catsandog",["cats","dog","sand","and","cat"]))