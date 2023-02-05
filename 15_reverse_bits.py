class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result << 1
            bit = n%2
            result += bit
            n = n >> 1
        return result

a = Solution()
print(a.reverseBits(43261596))
print(a.reverseBits(4294967293))

'''
The algorithm in plain english –

1. Do the following 32 times (because we have 32 bit integer)
2. left shift res by 1
3. add n%2 to res
4. right shift n by 1

A simple example –

# Input: 1010

#    res<<1     res+=n%2      n>>1
#           00                  00        101
#         000                001          10
#       0010             0010             1
#     00100           00101             _
'''

'''
Another solution:
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))
        return result
'''