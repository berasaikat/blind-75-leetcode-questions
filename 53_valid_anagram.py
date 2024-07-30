class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(t) == sorted(s)
    
a = Solution()
print(a.isAnagram("anagram", "nagaram"))
print(a.isAnagram("rat", "car"))

'''
Assuming sorting takes no extra space, the space complexity of above code is O(1).
The space complexity of below code is O(len(s)+len(t)).
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter_s, counter_t = {}, {}
        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        for i in counter_s:
            if counter_s[i] != counter_t.get(i, 0):
                return False
        return True  
------------------------------------------------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(t) == Counter(s)
'''