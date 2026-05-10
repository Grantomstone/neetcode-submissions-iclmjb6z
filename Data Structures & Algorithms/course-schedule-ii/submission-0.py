class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for k, v in prerequisites:
            preMap[k].append(v)
        
        visiting, cycle = set(), set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visiting:
                return True

            cycle.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visiting.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
            
        return output