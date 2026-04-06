"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        mapping = {}
        startTimes = []
        
        
        for i in intervals:
            startTimes.append(i.start)
            mapping[i.start] = mapping.get(i.start, None)
            if mapping[i.start]:
                return False
            mapping[i.start] = i

        startTimes = sorted(startTimes)

        for i in range(len(startTimes)-1):
            start= startTimes[i]
            end = mapping[start].end
            nextStart = startTimes[i+1]
            nextEnd = mapping[nextStart].end

            if  end>nextStart:
                return False
            
        
        return True


