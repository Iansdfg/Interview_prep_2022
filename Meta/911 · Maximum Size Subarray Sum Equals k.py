class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def max_sub_array_len(self, nums, k):
        # Write your code here
        prefix_index = {0:-1}#case when k == sum
        prefix_sum = 0
        ans = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            diff = prefix_sum - k 
            if prefix_sum not in prefix_index:
                prefix_index[prefix_sum] = i
                
            if diff in prefix_index:
                ans = max(ans, i - prefix_index[diff])

            
        return ans 


