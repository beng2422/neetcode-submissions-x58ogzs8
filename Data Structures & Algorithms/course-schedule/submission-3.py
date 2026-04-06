class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(numCourse):
            queue = [numCourse]
            seen = []
            courses = set()
            courses.add(numCourse)

            while queue:
                numCourse = queue[0]
                queue = queue[1:]

                for i in range(len(prerequisites)):
                    if numCourse == prerequisites[i][0]:
                        if i in seen:
                            return False
                        seen.append(i)
                        queue.append(prerequisites[i][1])
                        courses.add(numCourse)
            return courses

        totalSeen = set()
        for i in range((numCourses)):
            if i not in totalSeen:
                res = dfs(i)
                if res == False:
                    return False
                totalSeen = totalSeen.union(res)
        return True
