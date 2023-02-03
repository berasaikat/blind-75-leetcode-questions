class Solution(object):
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n &= (n - 1)
            result += 1
        return result

a = Solution()
print(a.hammingWeight(11))  #00000000000000000000000000001011
print(a.hammingWeight(128))  #00000000000000000000000010000000
print(a.hammingWeight(4294967293))  #11111111111111111111111111111101

'''
class Solution(object):
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result
'''