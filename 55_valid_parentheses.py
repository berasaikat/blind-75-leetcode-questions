class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        checklist = {")" : "(", "}" : "{", "]" : "["}
        for i in s:
            if i in checklist:
                if stack and stack[-1] == checklist[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
    
a = Solution()
print(a.isValid("()"))
print(a.isValid("()[]{}"))
print(a.isValid("(]"))
                
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        i = 0
        count = 0
        while i < len(l)-1:
            if l[i]=="(":
                if l[i+1]==")":
                    pass
                else:
                    count += 1
            elif l[i]=="{":
                if l[i+1]=="}":
                    pass
                else:
                    count += 1
            elif l[i]=="[":
                if l[i+1]=="]":
                    pass
                else:
                    count += 1
        if count == 0:
            return True
        return False
'''