class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        HashMap = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            HashMap[course].append(prerequisite)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if HashMap[course] == []:
                return True
            visit.add(course)
            for prerequisite in HashMap[course]:
                if not dfs(prerequisite): return False
            visit.remove(course)
            HashMap[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True
    
a = Solution()
print(a.canFinish(2,[[1,0]]))
print(a.canFinish(2,[[1,0],[0,1]]))