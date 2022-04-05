from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals):
        # Write your code here
        if not intervals:
            return True 
        intervals = sorted(intervals, key = lambda intervals:intervals.start )

        prev_interval = intervals[0]
        max_end = prev_interval.end
        for i in range(1, len(intervals)):
            if intervals[i].start >= max_end :
                prev_interval = intervals[i]
                max_end = max(max_end, intervals[i].end)
            else:
                print(intervals[i].start, intervals[i].end, max_end)
                return False 
        return True 



