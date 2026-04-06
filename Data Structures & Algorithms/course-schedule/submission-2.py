class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        def dfs(numCourse):
            queue = [numCourse]
            seen = []
            courses = set()
            courses.add(numCourse)
            inqueue = {numCourse}     # NEW: nodes currently in the frontier
            processed = set()         # NEW: nodes fully popped

            while queue:
                numCourse = queue[0]
                queue = queue[1:]
                inqueue.discard(numCourse)
                processed.add(numCourse)
                for i in range(len(prerequisites)):

                    if numCourse == prerequisites[i][0]:
                        if i in seen:
                            return False
                        seen.append(i)
                        queue.append(prerequisites[i][1])
                        courses.add(numCourse)
                        v = prerequisites[i][1]

                        if v in inqueue:        # NEW: back-edge ⇒ cycle
                            return False
                        if v not in processed:  # NEW: only enqueue if not done
                            queue.append(v)
                            inqueue.add(v)
                            courses.add(v)
            return courses
        totalSeen = set()
        for i in range((numCourses)):
            if i not in totalSeen:
                res = dfs(i)
                if res == False:
                    return False
                totalSeen = totalSeen.union(res)
        return True
                    