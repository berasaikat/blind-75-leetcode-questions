class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        result = 0
        i = 0
        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)
            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
        return result
    
a = Solution()
print(a.characterReplacement("ABAB", 2))
print(a.characterReplacement("AABABBA", 1))

'''
Time complexity: O(n) rather than O(26*n)
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        result = 0
        i = 0
        maxf = 0
        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)
            maxf = max(maxf, count[s[j]])
            while (j - i + 1) - maxf > k:
                count[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
        return result
'''