class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def least_interval(self, tasks, n):
        # write your code here
        task_cnt = dict()
        for task in tasks:
            if task not in task_cnt:
                task_cnt[task] = 0
            task_cnt[task] += 1 
        M = max(task_cnt.values())

        M_cnt = 0
        for key in task_cnt:
            if task_cnt[key] == M:
                M_cnt += 1
        
        return max(len(tasks), (M-1)*n + M + (M_cnt -1))

