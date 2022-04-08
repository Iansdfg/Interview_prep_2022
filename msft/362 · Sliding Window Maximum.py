from collections import deque

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def max_sliding_window(self, nums, k):
        # write your code here
        if not nums:
            return []
        slow, fast = 0, 0 
        q = deque([])
        res = []
        while fast < len(nums):
            new_item = nums[fast]
            fast += 1

            while q and q[-1] < new_item:
                    q.pop()
            q.append(new_item)

            while fast - slow > k:   
                left_item = nums[slow] 
                slow += 1 
                if left_item == q[0] and len(q) > 1:
                    q.popleft()

            if fast - slow == k:
                res.append(q[0])

    
        return res 

