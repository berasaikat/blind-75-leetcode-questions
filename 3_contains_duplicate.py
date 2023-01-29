class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        for i, n in enumerate(nums):
            if n in hash:
                return True
            hash[n] = i
        return False

a = Solution()
print(a.containsDuplicate([1,2,3,1]))
print(a.containsDuplicate([1,2,3,4]))
print(a.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))