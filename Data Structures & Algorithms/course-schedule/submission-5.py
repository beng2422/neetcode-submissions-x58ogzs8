class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(numCourse):
            visited = set()
            path = set()
            
            def hasCycle(course):
                if course in path:  
                    return True
                if course in visited: 
                    return False
                    
                visited.add(course)
                path.add(course)
                
                for prereq_course, prereq in prerequisites:
                    if prereq_course == course:
                        if hasCycle(prereq):
                            return True
                
                path.remove(course) 
                return False
            
            if hasCycle(numCourse):
                return False
            
            queue = [numCourse]
            courses = set()
            seen = set()

            while queue:
                current = queue.pop(0)
                if current in seen:
                    continue
                seen.add(current)
                courses.add(current)

                for prereq_course, prereq in prerequisites:
                    if prereq_course == current:
                        queue.append(prereq)
                        
            return courses

        totalSeen = set()
        for i in range((numCourses)):
            if i not in totalSeen:
                res = dfs(i)
                if res == False:
                    return False
                totalSeen = totalSeen.union(res)
        return True
