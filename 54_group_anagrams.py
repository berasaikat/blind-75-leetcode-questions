from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()
    
a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(a.groupAnagrams([""]))
print(a.groupAnagrams(["a"]))