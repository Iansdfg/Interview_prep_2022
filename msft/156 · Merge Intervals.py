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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda interval: interval.start)

        res = []
        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            if self.need_merge(prev_interval, intervals[i]):
                prev_interval = self.merge_helper(prev_interval, intervals[i])
            else:
                res.append(prev_interval)
                prev_interval = intervals[i]
        res.append(prev_interval)
        return res 

    def need_merge(self, a, b):
        return max(a.start, b.start) <= min(a.end, b.end);

    def merge_helper(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))

        
