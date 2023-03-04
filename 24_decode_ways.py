class Solution(object):
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == '1' or 
            (s[i] == '2' and s[i+1] in '0123456'))):
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
    
a = Solution()
print(a.numDecodings('12'))
print(a.numDecodings('226'))
print(a.numDecodings('06'))

'''
I got this O(1) space solution from the internet:

Very detailed O(1) Space solution & explanation below. Imagine we were using a dictionary as we do in our O(N) solution. len(s): 1 is our base case. When we start the tabulation solution, in our first loop, if s[i] != 0, we perform dp[i] = dp[i+1] to get 1. 

So to explain our variables, picture we're accessing indices just like that, just without a dictionary.

- dp_cur = dp[i]
- dp_plus1 = dp[i+1] (that's why this is initially declared with a 1, if you look again at the O(N) code)
- dp_plus2 = dp[i+2]

A couple short points:

- One quick clean up - instead of 'in '0123456'', we can just rewrite our code to <= '6'. 
- dp_cur += dp_plus1 is the equivalent of dp[i] = dp[i+1], because notice how at the end of each loop, dp_cur = 0.

Now for the main part in this code, which is the tricky part:

	dp_plus2 = dp_plus1
	dp_plus1 = dp_cur
	dp_cur = 0

Imagine these variables playing a game of 'baton pass', and let's use an input example of '226', looping in reverse.

1) In our first loop at number '6', we start with dp_plus1 as 1 as our base case. That gets passed to dp_plus2, because for our following loop our 'i'th index will be len(s) - 2, which will be the first time we can consider using dp_plus2 if we have a valid 2-length number. 

2) Now we look at the middle '2'. dp_plus1 and dp_plus2 are both equal to 1 at this point, and because both '2' and '26' are valid, we can add those to dp_cur, which now equals 2. That gets then updated to dp_plus1, and importantly,  our subproblems we've gotten from dp_plus2 are being passed THROUGH dp_cur TO dp_plus1 when we have a valid 2 digit number (dp += dp_plus2). Another important observation is, at this stage in the loop, dp_plus1 = 2, and dp_plus2 = 1. dp_plus1 is the correct number of valid subproblems so far. 

3) We can then cumulate all of those on our final '2', because '2' and '22' are both valid. dp_plus1 = 2, dp_plus2 = 1, add the two together and dp_cur = 3. dp_plus2 is carried from dp_plus1, so dp_plus2 = 2, because by this point, 2 valid double-digit subproblems are '22' and '26'. We update dp_plus1 to 3 from dp_cur, because there are 3 valid subproblems.

4) As noted in the last couple points, we return dp_plus1, as it's the base case, the "pivot" of this game of baton pass. 3 is the correct number of valid subproblems for '226'. 

Edge case with 0s: take "330012" as an example input. Our code returns 0, which is correct, because when we have 2 or more consecutive 0s there are NO valid solutions. '01' is not valid. '00' is not valid. '0' and '0' is not valid. '30' would be, but then '0' or again, '01', is not. 

Passes all test cases.

SOLUTION CODE:
class Solution:
	def numDecodings(self, s):
		dp_cur, dp_plus1, dp_plus2 = 0, 1, 0
		for i in range(len(s) -1, -1, -1):
			if s[i] != '0':
				dp_cur += dp_plus1
			if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
				dp_cur += dp_plus2
			dp_plus2 = dp_plus1
			dp_plus1 = dp_cur
			dp_cur = 0
		return dp_plus1
'''