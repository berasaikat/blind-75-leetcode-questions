class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cset = set()
        i = 0
        result = 0
        for j in range(len(s)):
            while s[j] in cset:
                cset.remove(s[i])
                i += 1
            cset.add(s[j])
            result = max(result, j - i + 1)
        return result
    
a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))
print(a.lengthOfLongestSubstring("pwwkew"))