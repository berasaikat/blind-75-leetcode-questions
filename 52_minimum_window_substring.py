class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "": return ""
        count_t, window = {}, {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        have, need = 0, len(count_t)
        res_len, result = float("infinity"), [-1, -1]
        i = 0
        for j in range(len(s)):
            window[s[j]] = 1 + window.get(s[j], 0)
            if s[j] in count_t and count_t[s[j]] == window[s[j]]:
                have += 1
            while need == have:
                if (j - i + 1) < res_len:
                    res_len = j - i + 1
                    result = [i, j]
                window[s[i]] -= 1
                if s[i] in count_t and count_t[s[i]] > window[s[i]]:
                    have -= 1
                i += 1
        i, j = result
        return s[i:j+1] if res_len != float("infinity") else ""
    
a = Solution()
print(a.minWindow("ADOBECODEBANC", "ABC"))
print(a.minWindow("a", "a"))
print(a.minWindow("a", "aa"))