class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        def palindrom(left, right, s):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            return result

        for i in range(len(s)):
            left = right = i
            result += palindrom(left, right, s)
            left = i
            right = i + 1
            result += palindrom(left, right, s)
        return result
    
a = Solution()
print(a.countSubstrings("abc"))
print(a.countSubstrings("aaa"))