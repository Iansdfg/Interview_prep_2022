class Solution:
    """
    @param logs: the logs
    @return: the logs after sorting
    """
    def log_sort(self, logs):
        # Write your code here
        with_int = []
        with_str = []
        for log in logs:
            split_log = log.split(' ')
            if split_log[-1].isdigit():
                with_int.append(log)
            else:
                index = log.index(' ')
                with_str.append((log, log[index + 1:], log[:index]))
        
        with_str.sort(key = lambda x: (x[1], x[2]))
        with_str = [ele[0] for ele in with_str]

        return with_str + with_int


 
